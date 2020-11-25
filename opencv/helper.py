# -*- coding: utf-8 -*-
import time
import sys
import os
import six
import traceback
import win32gui
import win32api
import win32ui
import win32con
from airtest.aircv.utils import Image, pil_2_cv2
from airtest.core.settings import Settings as ST
from airtest.utils.logwraper import Logwrap, AirtestLogger
from airtest.utils.logger import get_logger
from airtest.aircv import cv2

class G(object):
    """Represent the globals variables"""
    BASEDIR = []
    LOGGER = AirtestLogger(None)
    LOGGING = get_logger("airtest.core.api")
    SCREEN = None
    DEVICE = None
    DEVICE_LIST = []
    RECENT_CAPTURE = None
    RECENT_CAPTURE_PATH = None
    CUSTOM_DEVICES = {}

    @classmethod
    def snapshot(self, filename=None):
        self._gen_screen_log(filename=filename)

    @classmethod
    def _gen_screen_log(self, element=None, filename=None):
        if ST.LOG_DIR is None:
            return None
        if filename:
            self.screenshot(filename)
        jpg_file_name = str(int(time.time())) + '.jpg'
        jpg_path = os.path.join(ST.LOG_DIR, jpg_file_name)
        print("this is jpg path:", jpg_path)
        self.screenshot(jpg_path)
        saved = {"screen": jpg_file_name}
        if element:
            size = element.size
            location = element.location
            x = size['width'] / 2 + location['x']
            y = size['height'] / 2 + location['y']
            if "darwin" in sys.platform:
                x, y = x * 2, y * 2
            saved.update({"pos": [[x, y]]})
        return saved

    @classmethod
    def screenshot(filename, hwnd=None):
        """
        Take the screenshot of Windows app

        Args:
            filename: file name where to store the screenshot
            hwnd:

        Returns:
            bitmap screenshot file

        """
        # import ctypes
        # user32 = ctypes.windll.user32
        # user32.SetProcessDPIAware()

        if hwnd is None:
            """all screens"""
            hwnd = win32gui.GetDesktopWindow()
            # get complete virtual screen including all monitors
            w = win32api.GetSystemMetrics(SM_CXVIRTUALSCREEN)
            h = win32api.GetSystemMetrics(SM_CYVIRTUALSCREEN)
            x = win32api.GetSystemMetrics(SM_XVIRTUALSCREEN)
            y = win32api.GetSystemMetrics(SM_YVIRTUALSCREEN)
        else:
            """window"""
            rect = win32gui.GetWindowRect(hwnd)
            w = abs(rect[2] - rect[0])
            h = abs(rect[3] - rect[1])
            x, y = 0, 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (x, y), win32con.SRCCOPY)
        # saveBitMap.SaveBitmapFile(saveDC, filename)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        pil_image = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        cv2_image = pil_2_cv2(pil_image)

        mfcDC.DeleteDC()
        saveDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        # cv2.imshow('toolIcon',cv2_image)
        # cv2.waitKey(0)
        return cv2_image
    @classmethod
    def add_device(cls, dev):
        """
        Add device instance in G and set as current device.

        Examples:
            G.add_device(Android())

        Args:
            dev: device to init

        Returns:
            None

        """
        cls.DEVICE = dev
        cls.DEVICE_LIST.append(dev)

    @classmethod
    def register_custom_device(cls, device_cls):
        cls.CUSTOM_DEVICES[device_cls.__name__.lower()] = device_cls


"""
helper functions
"""


def set_logdir(dirpath):
    """set log dir for logfile and screenshots.

    Args:
        dirpath: directory to save logfile and screenshots

    Returns:

    """
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    ST.LOG_DIR = dirpath
    G.LOGGER.set_logfile(os.path.join(ST.LOG_DIR, ST.LOG_FILE))


def log(arg, trace=""):
    """
    Insert user log, will be displayed in Html report.

    :param data: log message or Exception
    :param trace: log traceback if exists, use traceback.format_exc to get best format
    :return: None
    """
    if G.LOGGER:
        if isinstance(arg, Exception):
            G.LOGGER.log("info", {
                    "name": arg.__class__.__name__,
                    "traceback": ''.join(traceback.format_exception(type(arg), arg, arg.__traceback__))
                })
        elif isinstance(arg, six.string_types):
            G.LOGGER.log("info", {"name": arg, "traceback": trace}, 0)
        else:
            raise TypeError("arg must be Exception or string")


def logwrap(f):
    return Logwrap(f, G.LOGGER)


def device_platform(device=None):
    if not device:
        device = G.DEVICE
    return device.__class__.__name__


def using(path):
    if not os.path.isabs(path):
        abspath = os.path.join(ST.PROJECT_ROOT, path)
        if os.path.exists(abspath):
            path = abspath
    G.LOGGING.debug("using path: %s", path)
    if path not in sys.path:
        sys.path.append(path)
    G.BASEDIR.append(path)


def import_device_cls(platform):
    """lazy import device class"""
    platform = platform.lower()
    if platform in G.CUSTOM_DEVICES:
        cls = G.CUSTOM_DEVICES[platform]
    elif platform == "android":
        from airtest.core.android.android import Android as cls
    elif platform == "windows":
        from airtest.core.win.win import Windows as cls
    elif platform == "ios":
        from airtest.core.ios.ios import IOS as cls
    elif platform == "linux":
        from airtest.core.linux.linux import Linux as cls
    else:
        raise RuntimeError("Unknown platform: %s" % platform)
    return cls


def delay_after_operation():
    time.sleep(ST.OPDELAY)
