from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_title = page.locator(".title")
        self.cart_item = page.locator(".cart_item")
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def get_cart_title(self):
        return self.cart_title

    def get_cart_item(self):
        return self.cart_item

    def click_checkout(self):
        self.checkout_button.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()