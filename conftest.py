import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.settings import ENVIRONMENTS
from pathlib import Path
from pages.file_upload_page import FileUploadPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page: Page, login_page: LoginPage, app_config):
    login_page.open(app_config["base_url"])
    login_page.login(
        app_config["valid_username"],
        app_config["valid_password"]
    )

    return page


@pytest.fixture
def inventory_page(authenticated_page: Page):
    return InventoryPage(authenticated_page)


@pytest.fixture
def cart_page(authenticated_page: Page):
    return CartPage(authenticated_page)


@pytest.fixture
def checkout_page(authenticated_page: Page):
    return CheckoutPage(authenticated_page)

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against: qa, staging, or prod"
    )


@pytest.fixture
def app_config(request):
    env_name = request.config.getoption("--env")

    if env_name not in ENVIRONMENTS:
        raise ValueError(f"Invalid environment: {env_name}")

    return ENVIRONMENTS[env_name]

@pytest.fixture
def authenticated_page(browser, app_config):
    auth_file = Path("auth/auth_state.json")

    if not auth_file.exists():
        raise FileNotFoundError(
            "auth/auth_state.json not found. Run: python -m pytest tests/test_auth_setup.py -v --env=qa"
        )

    context = browser.new_context(storage_state=str(auth_file))
    page = context.new_page()

    page.goto(app_config["base_url"] + "inventory.html")

    yield page

    context.close()
    
@pytest.fixture
def file_upload_page(page: Page):
    return FileUploadPage(page)