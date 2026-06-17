import pytest
import allure
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Save test failed status
    if report.when == "call":
        item.test_failed = report.failed

        if report.failed:
            page = item.funcargs.get("page") or item.funcargs.get("authenticated_page")

            if page:
                screenshots_dir = Path("allure-results/screenshots")
                screenshots_dir.mkdir(parents=True, exist_ok=True)

                screenshot_path = screenshots_dir / f"{item.name}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)

                allure.attach.file(
                    str(screenshot_path),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

    # Attach trace after Playwright teardown creates trace.zip
    if report.when == "teardown" and getattr(item, "test_failed", False):
        test_results_dir = Path("test-results")

        if test_results_dir.exists():
            trace_files = list(test_results_dir.rglob("trace.zip"))

            if trace_files:
                latest_trace = max(trace_files, key=lambda file: file.stat().st_mtime)

                allure.attach.file(
                    str(latest_trace),
                    name="Playwright Trace",
                    attachment_type="application/zip",
                    extension="zip"
                )