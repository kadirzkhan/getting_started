from playwright.sync_api import Page, expect
import time

def test_accept_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept())

    page.locator("button", has_text="Click for JS Alert").click()
    time.sleep(3)

    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")


def test_accept_confirm(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept())

    page.locator("button", has_text="Click for JS Confirm").click()
    
    time.sleep(3)

    expect(page.locator("#result")).to_have_text("You clicked: Ok")


def test_dismiss_confirm(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.dismiss())

    page.locator("button", has_text="Click for JS Confirm").click()
    time.sleep(3)

    expect(page.locator("#result")).to_have_text("You clicked: Cancel")


def test_prompt_with_text(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept("Hello, Abdul!"))

    page.locator("button", has_text="Click for JS Prompt").click()
    
    time.sleep(3)

    expect(page.locator("#result")).to_have_text("You entered: Hello, Abdul!")