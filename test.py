from playwright.sync_api import Page, expect

def test_valid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.pause()

    page.locator("#user-name").fill("standard_user")