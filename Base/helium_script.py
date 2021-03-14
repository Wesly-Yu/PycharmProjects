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
    def 测试2(self):
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        start_chrome('www.baidu.com',headless=False,options=options)
        write('qq邮箱')
        press(ENTER)
        click('登录QQ邮箱')
        #go_to('https://mail.qq.com/')
        write("1633235633@qq.com", into='#username')
        write("ChuanA52sg0743799.com", into='#password')
        sleep(3000)
        wait_until('pp',3000,2)
        write("yu1234567", into='password')
        click(Text('登录'))
        kill_browser()
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(play_wright('测试1'))
    # suite.addTest(play_wright('test_c'))
    runner = unittest.TextTestRunner()
    runner.run(suite)