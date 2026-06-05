from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_to_cart_backpack_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_page_title(self):
        return self.page_title

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack_button.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack_button.click()

    def open_cart(self):
        self.cart_icon.click()

    def get_cart_badge(self):
        return self.cart_badge