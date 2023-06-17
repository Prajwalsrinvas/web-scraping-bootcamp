from playwright.sync_api import sync_playwright

url = "https://store.steampowered.com/specials"


def fetch_page():
    print("[x] Fetching page")
    with sync_playwright() as p:
        headless = True
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(url)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_load_state("networkidle")
        data = page.content()
        browser.close()
    return data
