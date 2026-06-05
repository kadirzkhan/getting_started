from playwright.sync_api import Page, expect
import pages
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login_page = pages.login_page.LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(page: Page):
    login_page = pages.login_page.LoginPage(page)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )