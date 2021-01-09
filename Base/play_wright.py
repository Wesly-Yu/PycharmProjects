import pytest
from time import sleep
from playwright import sync_playwright


playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.newPage()
page.goto("https://www.baidu.com")
page.type("input[id=kw]", "Playwright GitHub")
page.click("input[id=su]")
sleep(3)
page.screenshot(path="example.png")
page.close()
playwright.stop()
#
# def test_visit_admin_dashboard():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.newPage()
#         page.goto("https://www.baidu.com")
#         page.type("input[id=kw]", "Playwright GitHub")
#         page.click("input[id=su]")
#         sleep(3)
#         page.close()
#
# if __name__ == '__main__':
#     test_visit_admin_dashboard()