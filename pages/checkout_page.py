from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.checkout_title = page.locator(".title")
        self.success_message = page.locator(".complete-header")
        self.error_message = page.locator('[data-test="error"]')

    def verify_checkout_information_page(self):
        self.verify_text(self.checkout_title, "Checkout: Your Information")

    def enter_first_name(self, first_name: str):
        self.fill_text(self.first_name_input, first_name)

    def enter_last_name(self, last_name: str):
        self.fill_text(self.last_name_input, last_name)

    def enter_postal_code(self, postal_code: str):
        self.fill_text(self.postal_code_input, postal_code)

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.click_element(self.continue_button)

    def verify_checkout_overview_page(self):
        self.verify_text(self.checkout_title, "Checkout: Overview")

    def click_finish(self):
        self.click_element(self.finish_button)

    def verify_order_success_message(self):
        self.verify_text(self.success_message, "Thank you for your order!")
        
    def verify_checkout_error_message(self, expected_error: str):
     self.verify_partial_text(self.error_message, expected_error)