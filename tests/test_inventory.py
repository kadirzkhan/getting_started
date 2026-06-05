from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


def test_inventory_page_title_after_login(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.get_page_title()).to_have_text("Products")


def test_add_product_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.get_cart_badge()).to_have_text("1")


def test_remove_product_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    expect(inventory_page.get_cart_badge()).to_have_text("1")

    inventory_page.remove_backpack_from_cart()

    expect(inventory_page.get_cart_badge()).not_to_be_visible()