import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config.settings import INVALID_USERNAME, INVALID_PASSWORD

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(page: Page, app_config):
    login_page = LoginPage(page)

    login_page.open(app_config["base_url"])
    login_page.login(
        app_config["valid_username"],
        app_config["valid_password"]
    )

    expect(page).to_have_url(app_config["base_url"] + "inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

@pytest.mark.regression
@pytest.mark.login
def test_invalid_login(page: Page, app_config):
    login_page = LoginPage(page)

    login_page.open(app_config["base_url"])
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )