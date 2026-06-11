from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_title = page.locator(".title")
        self.cart_item = page.locator(".cart_item")
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def verify_cart_page_title(self):
        self.verify_text(self.cart_title, "Your Cart")

    def verify_cart_item_visible(self):
        self.verify_visible(self.cart_item)

    def click_checkout(self):
        self.click_element(self.checkout_button)

    def click_continue_shopping(self):
        self.click_element(self.continue_shopping_button)

    def verify_checkout_button_visible(self):
        self.verify_visible(self.checkout_button)

    def get_cart_title(self):
        return self.cart_title

    def get_cart_item(self):
        return self.cart_item