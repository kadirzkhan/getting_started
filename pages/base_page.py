from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url)

    def click_element(self, locator: Locator):
        expect(locator).to_be_visible()
        locator.click()

    def fill_text(self, locator: Locator, text: str):
        expect(locator).to_be_visible()
        locator.fill(text)

    def get_text(self, locator: Locator):
        expect(locator).to_be_visible()
        return locator.inner_text()

    def verify_text(self, locator: Locator, expected_text: str):
        expect(locator).to_have_text(expected_text)

    def verify_partial_text(self, locator: Locator, expected_text: str):
        expect(locator).to_contain_text(expected_text)

    def verify_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def verify_not_visible(self, locator: Locator):
        expect(locator).not_to_be_visible()

    def take_screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)