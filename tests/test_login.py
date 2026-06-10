from playwright.sync_api import Page, expect
import pages
from pages.login_page import LoginPage
from config.settings import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD, BASE_URL

def test_valid_login(page: Page):
    login_page = pages.login_page.LoginPage(page)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url(BASE_URL + "inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(page: Page):
    login_page = pages.login_page.LoginPage(page)

    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )