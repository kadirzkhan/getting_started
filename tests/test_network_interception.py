from playwright.sync_api import Page, expect


def test_block_images(page: Page):
    page.route(
        "**/*",
        lambda route: route.abort()
        if route.request.resource_type == "image"
        else route.continue_()
    )

    page.goto("https://www.saucedemo.com/")

    expect(page.locator("#login-button")).to_be_visible()