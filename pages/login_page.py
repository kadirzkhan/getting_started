from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self, base_url: str):
        self.open_url(base_url)

    def enter_username(self, username: str):
        self.fill_text(self.username_input, username)

    def enter_password(self, password: str):
        self.fill_text(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.error_message)

    def verify_error_message(self, expected_error: str):
        self.verify_partial_text(self.error_message, expected_error)