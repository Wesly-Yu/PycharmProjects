import os
import unittest
from time import sleep
from playwright import sync_playwright
from playwright import async_playwright
import pytest

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False)
# page = browser.newPage()
# page.goto("https://www.baidu.com")
# page.type("input[id=kw]", "Playwright GitHub")
# page.click("input[id=su]")
# sleep(3)
# page.screenshot(path="example.png")
# page.close()
# playwright.stop()
#
# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False)
# page = browser.newPage()
# page.goto("https://www.baidu.com")
# page.type("input[id=kw]", "Playwright GitHub")
# page.click("input[id=su]")
# sleep(3)
# page.screenshot(path="example.png")
# page.close()
# playwright.stop()


# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False)
# page = browser.newPage()
class play_wright(unittest.TestCase):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.newPage()

    def test_a(self):
        self.page.goto("https://www.baidu.com")
        self.page.type("input[id=kw]", "Playwright GitHub")
        self.page.click("input[id=su]")
        sleep(3)


    def test_c(self):
        self.page.fill("input[id=kw]",'')
        self.page.type("input[id=kw]", "ps5")
        self.page.click("input[id=su]")
        sleep(3)
        self.page.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(play_wright('test_a'))
    suite.addTest(play_wright('test_c'))
    runner = unittest.TextTestRunner()
    runner.run(suite)