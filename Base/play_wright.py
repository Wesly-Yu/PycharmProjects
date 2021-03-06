import os
import unittest
from time import sleep
from playwright import sync_playwright


class play_wright(unittest.TestCase):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.newContext().newPage()





    def test_a(self):
        self.page.goto("https://www.baidu.com")
        self.page.type("input[id=kw]", "Playwright GitHub")
        self.page.waitForTimeout(1000)
        self.page.click("input[id=su]")
        self.page.waitForTimeout(3000)
        text=self.page.querySelector('a[name="tj_login"]').textContent()
        print(text)
        self.page.waitForTimeout(3000)
        self.page.goBack()
        page2 = self.browser.newContext().newPage()
        page2.goto('https://google.com')
        self.page.bringToFront()
        self.page.waitForTimeout(3000)


    def test_c(self):
        self.page.setViewportSize(width=1920,height=1080)
        self.page.fill("input[id=kw]",'')
        self.page.type("input[id=kw]", "ps5")
        self.page.waitForTimeout(1000)
        self.page.click("input[id=su]")
        self.page.waitForTimeout(3000)
        self.page.keyboard.down(key="ArrowDown")
        if self.page.waitForSelector("//a[contains(text(),'下一页 >')]", 5000,'visible'):
            self.page.waitForTimeout(3000)
            self.page.click("//a[contains(text(),'下一页 >')]")
        else:
            self.page.keyboard.down(key="ArrowDown")
        # self.page.querySelector('a[name="tj_login"]').waitForElementState('visible',5000)
        self.page.querySelector('a[name="tj_login"]').textContent()
        self.page.querySelector('a[name="tj_login"]')
        # self.page.waitForTimeout(3000)
        self.page.querySelector("//a[contains(text(),'下一页 >')]").scrollIntoViewIfNeeded()
        # self.page.waitForTimeout(2000)
        self.page.querySelector("//a[contains(text(),'下一页 >')]").scrollIntoViewIfNeeded()
        self.page.waitForTimeout(3000)
        # if self.page.waitForSelector('a[name="tj_login"]', 5000,'visible'):
        #     self.page.click('a[name="tj_login"]')
        #     self.page.waitForTimeout(3000)
        self.page.close()
    def test_d(self):
        self.page.setViewportSize(width=1920,height=1080)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(play_wright('test_a'))
    # suite.addTest(play_wright('test_c'))
    runner = unittest.TextTestRunner()
    runner.run(suite)