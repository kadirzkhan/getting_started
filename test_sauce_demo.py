from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_username(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("wrong_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.screenshot(path="debug_image/debug_login1.png")


    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password success match")


def test_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password do not match")


def test_empty_username(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username is required")


def test_empty_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#login-button").click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Password is required")
