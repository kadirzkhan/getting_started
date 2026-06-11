import pytest
from utils.data_reader import read_json_file


checkout_data = read_json_file("test_data/checkout_data.json")
negative_checkout_users = checkout_data["negative_checkout_users"]


def test_complete_checkout_flow(inventory_page, cart_page, checkout_page):
    user_data = checkout_data["valid_checkout_user"]

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.verify_cart_page_title()
    cart_page.verify_cart_item_visible()
    cart_page.click_checkout()

    checkout_page.verify_checkout_information_page()
    checkout_page.fill_checkout_information(
        user_data["first_name"],
        user_data["last_name"],
        user_data["postal_code"]
    )
    checkout_page.click_continue()

    checkout_page.verify_checkout_overview_page()
    checkout_page.click_finish()

    checkout_page.verify_order_success_message()


@pytest.mark.parametrize(
    "user_data",
    negative_checkout_users,
    ids=[item["test_name"] for item in negative_checkout_users]
)
def test_checkout_required_field_validation(inventory_page, cart_page, checkout_page, user_data):
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.verify_checkout_information_page()
    checkout_page.fill_checkout_information(
        user_data["first_name"],
        user_data["last_name"],
        user_data["postal_code"]
    )
    checkout_page.click_continue()

    checkout_page.verify_checkout_error_message(user_data["expected_error"])