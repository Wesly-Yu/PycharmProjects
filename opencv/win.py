# -*- coding: utf-8 -*-
import os
from mss import mss
from functools import wraps
import pywintypes  # noqa
import win32api
import time
from pykeyboard import PyKeyboard
from opencv.exceptions import IsNotTemplateError
from opencv.helper import G,logwrap
from pywinauto.application import Application
from pywinauto import mouse, keyboard
from pywinauto.win32structures import RECT
from airtest.core.settings import Settings as ST
from pywinauto.win32functions import SetForegroundWindow, GetSystemMetrics
from airtest.core.win.screen import screenshot
from airtest.core.error import TargetNotFoundError, InvalidMatchingMethodError
from airtest import aircv
from airtest.core.device import Device
from airtest.aircv import cv2
from airtest.utils.transform import TargetPos
from airtest.aircv.template_matching import TemplateMatching
from airtest.aircv.keypoint_matching import KAZEMatching, BRISKMatching, AKAZEMatching, ORBMatching
from airtest.aircv.keypoint_matching_contrib import SIFTMatching, SURFMatching, BRIEFMatching
from opencv.cv import Template

MATCHING_METHODS = {
    "tpl": TemplateMatching,
    "kaze": KAZEMatching,
    "brisk": BRISKMatching,
    "akaze": AKAZEMatching,
    "orb": ORBMatching,
    "sift": SIFTMatching,
    "surf": SURFMatching,
    "brief": BRIEFMatching,
}

def require_app(func):
    @wraps(func)
    def wrapper(inst, *args, **kwargs):
        if not inst.app:
            raise RuntimeError("Connect to an application first to use %s" % func.__name__)
        return func(inst, *args, **kwargs)
    return wrapper


class Windows(Device):
    """Windows client."""


    def __init__(self, handle=None, dpifactor=1, **kwargs):
        super(Windows, self).__init__()
        self.app = None
        self.handle = int(handle) if handle else None
        self._dpifactor = float(dpifactor)
        self._app = Application()
        self._top_window = None
        self._focus_rect = (0, 0, 0, 0)
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = mss()
        self.monitor = self.screen.monitors[0]  # 双屏的时候，self.monitor为整个双屏
        self.main_monitor = self.screen.monitors[1]  # 双屏的时候，self.main_monitor为主屏

    @logwrap
    def loop_find(self,query, timeout=ST.FIND_TIMEOUT, threshold=None, interval=0.5, intervalfunc=None):
        G.LOGGING.info("Try finding:\n%s", query)
        start_time = time.time()
        while True:
            screen = self.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)

            if screen is None:
                G.LOGGING.warning("Screen is None, may be locked")
            else:
                if threshold:
                    query.threshold = threshold
                match_pos = query.match_in(screen)
                if match_pos:
                    self.try_log_screen(screen)
                    return match_pos

            if intervalfunc is not None:
                intervalfunc()

            # 超时则raise，未超时则进行下次循环:
            if (time.time() - start_time) > timeout:
                self.try_log_screen(screen)
                raise TargetNotFoundError('Picture %s not found in screen' % query)
            else:
                time.sleep(interval)

    @logwrap
    def try_log_screen(self,screen=None):
        """
        Save screenshot to file

        Args:
            screen: screenshot to be saved

        Returns:
            None

        """
        if not ST.LOG_DIR:
            return
        if screen is None:
            screen = self.snapshot(quality=ST.SNAPSHOT_QUALITY)
        filename = "%(time)d.jpg" % {'time': time.time() * 1000}
        print(filename)
        filepath = os.path.join(ST.LOG_DIR, filename)
        aircv.imwrite(filepath, screen, ST.SNAPSHOT_QUALITY)
        return {"screen": filename, "resolution": aircv.get_resolution(screen)}

    def snapshot(self, filename=None, quality=10):
        """
        Take a screenshot and save it in ST.LOG_DIR folder

        Args:
            filename: name of the file to give to the screenshot, {time}.jpg by default
            quality: The image quality, integer in range [1, 99]

        Returns:
            display the screenshot

        """
        if self.handle:
            screen = screenshot(filename, self.handle)
        else:
            screen = screenshot(filename)
            if self.app:
                rect = self.get_rect()
                screen = aircv.crop_image(screen, [rect.left, rect.top, rect.right, rect.bottom])
        if not screen.any():
            if self.app:
                rect = self.get_rect()
                screen = aircv.crop_image(screenshot(filename), [rect.left, rect.top, rect.right, rect.bottom])
        if self._focus_rect != (0, 0, 0, 0):
            height, width = screen.shape[:2]
            rect = (self._focus_rect[0], self._focus_rect[1], width + self._focus_rect[2], height + self._focus_rect[3])
            screen = aircv.crop_image(screen, rect)
        if filename:
            aircv.imwrite(filename, screen, quality)
        return screen

    def keyevent(self, keyname, **kwargs):
        """
        Perform a key event

        References:
            https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html

        Args:
            keyname: key event
            **kwargs: optional arguments

        Returns:
            None

        """
        self.keyboard.SendKeys(keyname)

    def text(self, text, **kwargs):
        """
        Input text

        Args:
            text: text to input
            **kwargs: optional arguments

        Returns:
            None

        """
        self.keyevent(text)

    def _fix_op_pos(self, pos):
        """Fix operation position."""
        # 如果是全屏的话，就进行双屏修正，否则就正常即可
        if not self.handle:
            pos = list(pos)
            pos[0] = pos[0] + self.monitor["left"]
            pos[1] = pos[1] + self.monitor["top"]

        return pos

    def touch(self, pos, **kwargs):
        """
        Perform mouse click action

        References:
            https://pywinauto.readthedocs.io/en/latest/code/pywinauto.mouse.html

        Args:
            pos: coordinates where to click
            **kwargs: optional arguments

        Returns:
            None

        """
        duration = kwargs.get("duration", 0.01)
        right_click = kwargs.get("right_click", False)
        button = "right" if right_click else "left"
        steps = kwargs.get("steps", 1)
        offset = kwargs.get("offset", 0)

        start = self._action_pos(win32api.GetCursorPos())
        end = self._action_pos(pos)
        start_x, start_y = self._fix_op_pos(start)
        end_x, end_y = self._fix_op_pos(end)

        interval = float(duration) / steps
        time.sleep(interval)

        for i in range(1, steps):
            x = int(start_x + (end_x-start_x) * i / steps)
            y = int(start_y + (end_y-start_y) * i / steps)
            self.mouse.move(coords=(x, y))
            time.sleep(interval)

        self.mouse.move(coords=(end_x, end_y))

        for i in range(1, offset+1):
            self.mouse.move(coords=(end_x+i, end_y+i))
            time.sleep(0.01)

        for i in range(offset):
            self.mouse.move(coords=(end_x+offset-i, end_y+offset-i))
            time.sleep(0.01)

        self.mouse.press(button=button, coords=(end_x, end_y))
        time.sleep(duration)
        self.mouse.release(button=button, coords=(end_x, end_y))

    def double_click(self, pos):
        pos = self._fix_op_pos(pos)
        coords = self._action_pos(pos)
        self.mouse.double_click(coords=coords)

    def swipe(self, p1, p2, duration=0.8, steps=5):
        """
        Perform swipe (mouse press and mouse release)

        Args:
            p1: start point
            p2: end point
            duration: time interval to perform the swipe action
            steps: size of the swipe step

        Returns:
            None

        """
        # 设置坐标时相对于整个屏幕的坐标:
        x1, y1 = self._fix_op_pos(p1)
        x2, y2 = self._fix_op_pos(p2)

        from_x, from_y = self._action_pos(p1)
        to_x, to_y = self._action_pos(p2)

        interval = float(duration) / (steps + 1)
        self.mouse.press(coords=(from_x, from_y))
        time.sleep(interval)
        for i in range(1, steps):
            self.mouse.move(coords=(
                int(from_x + (to_x - from_x) * i / steps),
                int(from_y + (to_y - from_y) * i / steps),
            ))
            time.sleep(interval)
        for i in range(10):
            self.mouse.move(coords=(to_x, to_y))
        time.sleep(interval)
        self.mouse.release(coords=(to_x, to_y))

    def mouse_move(self, pos):
        """Simulates a `mousemove` event.

        Known bug:
            Due to a bug in the pywinauto module, users might experience \
            off-by-one errors when it comes to the exact coordinates of \
            the position on screen.

        :param pos: A tuple (x, y), where x and y are x and y coordinates of
                    the screen to move the mouse to, respectively.
        """
        if not isinstance(pos, tuple) or len(pos) != 2:  # pos is not a 2-tuple
            raise ValueError('invalid literal for mouse_move: {}'.format(pos))
        try:
            self.mouse.move(coords=self._action_pos(pos))
        except ValueError:  # in case where x, y are not numbers
            raise ValueError('invalid literal for mouse_move: {}'.format(pos))

    def mouse_down(self, button='left'):
        """Simulates a `mousedown` event.

        :param button: A string indicating which mouse button to be pressed.
                       Available mouse button options are:
                       {'left', 'middle', 'right'}.
        """
        buttons = {'left', 'middle', 'right'}
        if not isinstance(button, str) or button not in buttons:
            raise ValueError('invalid literal for mouse_down(): {}'.format(button))
        else:
            coords = self._action_pos(win32api.GetCursorPos())
            self.mouse.press(button=button, coords=coords)

    def mouse_up(self, button='left'):
        """Simulates a `mouseup` event.

        A call to the mouse_up() method usually follows a call to the
        mouse_down() method of the same mouse button.

        :param button: A string indicating which mouse button to be released.
        """
        buttons = {'left', 'middle', 'right'}
        if not isinstance(button, str) or button not in buttons:
            raise ValueError('invalid literal for mouse_up(): {}'.format(button))
        else:
            coords = self._action_pos(win32api.GetCursorPos())
            self.mouse.release(button=button, coords=coords)

    def get_rect(self):
        """
        Get rectangle

        Returns:
            win32structures.RECT

        """
        if self.app and self._top_window:
            return self._top_window.rectangle()
        else:
            return RECT(right=GetSystemMetrics(0), bottom=GetSystemMetrics(1))

    @require_app
    def get_title(self):
        """
        Get the window title

        Returns:
            window title

        """
        return self._top_window.texts()

    @require_app
    def get_pos(self):
        """
        Get the window position coordinates

        Returns:
            coordinates of topleft corner of the window (left, top)

        """
        rect = self.get_rect()
        return (rect.left, rect.top)

    def _action_pos(self, pos):
        if self.app:
            pos = self._windowpos_to_screenpos(pos)
        pos = (int(pos[0]), int(pos[1]))
        return pos

    # @property
    # def handle(self):
    #     return self._top_window.handle

    @property
    def focus_rect(self):
        return self._focus_rect

    @focus_rect.setter
    def focus_rect(self, value):
        # set focus rect to get rid of window border
        assert len(value) == 4, "focus rect must be in [left, top, right, bottom]"
        self._focus_rect = value

    def get_current_resolution(self):
        rect = self.get_rect()
        w = (rect.right + self._focus_rect[2]) - (rect.left + self._focus_rect[0])
        h = (rect.bottom + self._focus_rect[3]) - (rect.top + self._focus_rect[1])
        return w, h

    def _windowpos_to_screenpos(self, pos):
        """
        Convert given position relative to window topleft corner to screen coordinates

        Args:
            pos: coordinates (x, y)

        Returns:
            converted position coordinates

        """
        rect = self.get_rect()
        pos = (int((pos[0] + rect.left + self._focus_rect[0]) * self._dpifactor),
               int((pos[1] + rect.top + self._focus_rect[1]) * self._dpifactor))
        return pos

    # 点击输入框等，然后输入字符串
    def input_text(self, pos, text):
        self.touch(pos)
        self.pykeyboard.type_string(text)

    @logwrap
    def assert_template(self, v, msg=""):
        """
        Assert target exists on the current page.

        Args:
            v: target to touch, either a Template instance
        Raise:
            AssertionError - if target not found.
        Returns:
            Position of the template.
        """
        if isinstance(v, Template):
            try:
                pos = self.loop_find(v, timeout=ST.FIND_TIMEOUT)
            except TargetNotFoundError:
                raise AssertionError("Target template not found on screen.")
            else:
                return pos
        else:
            raise IsNotTemplateError("args is not a template")
'''----------------------------------------------------------------------------------------------------'''


if __name__ == "__main__":
    from selenium import webdriver
    chrome = webdriver.Chrome()
    page = chrome.get('http://www.baidu.com')
    chrome.maximize_window()
    win = Windows()
    time.sleep(3)
    chrome.find_element_by_id("kw").send_keys('cypress')
    time.sleep(2)
    position=win.loop_find(Template('baidu.png'))
    windows=Windows()
    windows.touch(position)
    time.sleep(10)
    chrome.quit()