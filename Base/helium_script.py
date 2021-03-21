import os
import unittest
from time import sleep
from helium import *
from selenium.webdriver import ChromeOptions,FirefoxOptions


class play_wright(unittest.TestCase):
    options = ChromeOptions()
    optionsFireFox = FirefoxOptions()
    options.add_argument('--start-maximized')

    def  测试1(self):
        start_chrome("https://www.zhihu.com/signin?next=%2F", options=self.options)
        click(Text("密码登录"))
        write("python@123.com", into=S("@username"))
        write("python", into="密码")
        click(Button("", below="登录"))
        press(ENTER)
        doubleclick("Double click here")
        doubleclick(Image("Directories"))
        scroll_up(num_pixels=100)
        scroll_down(num_pixels=100)
        rightclick("Something")
        select("Language", "English")
        attach_file("c:/test.txt", to="Please select a file:")
        refresh()
        wait_until(Text("Finished!").exists)
        wait_until(S("@username").exists)
        name=TextField("First name").value
        drag_file(r"C:\Documents\notes.txt", to="Drop files here")
        drag("Drag me!", to="Drop here.")
        get_driver().save_screenshot(r'C:\screenshot.png')
        Text("Do you want to proceed?").exists()

    def 测试2(self):
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        start_chrome('www.baidu.com',headless=False,options=options)
        wait_until(S("//input[@id='su']").exists)
        write('qq邮箱')
        sleep(5)
        get_driver().save_screenshot(r'C:\screenshot.png')
        press(ENTER)
        kill_browser()
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(play_wright('测试2'))
    # suite.addTest(play_wright('test_c'))
    runner = unittest.TextTestRunner()
    runner.run(suite)