from playwright import sync_playwright


def newPage(page):
    print("newPage() page title:", page.title())


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
    )
    context = browser.newContext()
    page = context.newPage()

    context.on("page", lambda page: newPage(page))

    page.evaluate('''() => {
        window.open('https://google.com', '_blank')
    }''')
    page.bringToFront()

    page.waitForTimeout(5000)
    browser.close()