from pathlib import Path
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_save_login_state(page: Page, app_config):
    auth_dir = Path("auth")
    auth_dir.mkdir(exist_ok=True)

    login_page = LoginPage(page)

    login_page.open(app_config["base_url"])
    login_page.login(
        app_config["valid_username"],
        app_config["valid_password"]
    )

    expect(page).to_have_url(app_config["base_url"] + "inventory.html")

    page.context.storage_state(path="auth/auth_state.json")