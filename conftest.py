import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.settings import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page: Page, login_page: LoginPage):
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return page


@pytest.fixture
def inventory_page(logged_in_page: Page):
    return InventoryPage(logged_in_page)


@pytest.fixture
def cart_page(logged_in_page: Page):
    return CartPage(logged_in_page)