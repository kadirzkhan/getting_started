from playwright.sync_api import Page, expect


def test_new_tab_opens(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as popup_info:
        page.locator("text=Click Here").click()

    new_page = popup_info.value

    expect(new_page.locator("h3")).to_have_text("New Window")
    