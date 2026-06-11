from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_to_cart_backpack_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        self.cart_badge = page.locator(".shopping_cart_badge")

    def verify_inventory_page_title(self):
        self.verify_text(self.page_title, "Products")

    def add_backpack_to_cart(self):
        self.click_element(self.add_to_cart_backpack_button)

    def remove_backpack_from_cart(self):
        self.click_element(self.remove_backpack_button)

    def open_cart(self):
        self.click_element(self.cart_icon)

    def verify_cart_badge_count(self, count: str):
        self.verify_text(self.cart_badge, count)

    def verify_cart_badge_not_visible(self):
        self.verify_not_visible(self.cart_badge)

    def get_page_title(self):
        return self.page_title

    def get_cart_badge(self):
        return self.cart_badge