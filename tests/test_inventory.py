def test_inventory_page_title_after_login(inventory_page):
    inventory_page.verify_inventory_page_title()


def test_add_product_to_cart(inventory_page):
    inventory_page.add_backpack_to_cart()

    inventory_page.verify_cart_badge_count("1")


def test_remove_product_from_cart(inventory_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.verify_cart_badge_count("1")

    inventory_page.remove_backpack_from_cart()

    inventory_page.verify_cart_badge_not_visible()