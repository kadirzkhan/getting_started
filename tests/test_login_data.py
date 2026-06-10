import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.data_reader import read_json_file


login_test_data = read_json_file("test_data/login_data.json")


@pytest.mark.parametrize("data", login_test_data, ids=[item["test_name"] for item in login_test_data])
def test_login_with_json_data(page: Page, data):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(data["username"], data["password"])

    if data["expected_result"] == "success":
        expect(page).to_have_url(data["expected_url"])
        expect(page.locator(".title")).to_have_text("Products")

    else:
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(data["expected_error"])