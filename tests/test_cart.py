import pytest


@pytest.mark.smoke
@pytest.mark.cart
def test_product_is_visible_in_cart(inventory_page, cart_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.verify_cart_page_title()
    cart_page.verify_cart_item_visible()

@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping_from_cart(inventory_page, cart_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.click_continue_shopping()

    inventory_page.verify_inventory_page_title()


def test_checkout_button_is_visible(inventory_page, cart_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.verify_checkout_button_visible()