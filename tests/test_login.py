import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config.settings import INVALID_USERNAME, INVALID_PASSWORD


@allure.feature("Login")
@allure.story("Valid user login")
@allure.title("Verify valid user can login successfully")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(page: Page, app_config):
    login_page = LoginPage(page)

    with allure.step("Open application login page"):
        login_page.open(app_config["base_url"])

    with allure.step("Login with valid username and password"):
        login_page.login(
            app_config["valid_username"],
            app_config["valid_password"]
        )

    with allure.step("Verify user is redirected to inventory page"):
        expect(page).to_have_url(app_config["base_url"] + "inventory.html")
        expect(page.locator(".title")).to_have_text("Products")


@allure.feature("Login")
@allure.story("Invalid user login")
@allure.title("Verify invalid user cannot login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.login
def test_invalid_login(page: Page, app_config):
    login_page = LoginPage(page)

    with allure.step("Open application login page"):
        login_page.open(app_config["base_url"])

    with allure.step("Login with invalid username and password"):
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do gfg match"
        )