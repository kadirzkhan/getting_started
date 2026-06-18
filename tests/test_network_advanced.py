from playwright.sync_api import Page, expect


def test_validate_api_response_using_playwright_request(page: Page):
    response = page.request.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status == 200

    body = response.json()

    assert body["id"] == 1
    assert body["username"] == "Bret"
    assert body["email"] == "Sincere@april.biz"


def test_wait_for_jsonplaceholder_api_response(page: Page):
    with page.expect_response(
        lambda response: "jsonplaceholder.typicode.com/users/1" in response.url
    ) as response_info:
        page.goto("https://jsonplaceholder.typicode.com/users/1")

    response = response_info.value

    assert response.status == 200

    body = response.json()

    assert body["id"] == 1
    assert body["username"] == "Bret"
    assert body["email"] == "Sincere@april.biz"


def test_saucedemo_login_navigation(page: Page, app_config):
    page.goto(app_config["base_url"])

    page.locator('[data-test="username"]').fill(app_config["valid_username"])
    page.locator('[data-test="password"]').fill(app_config["valid_password"])

    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(app_config["base_url"] + "inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_simulate_api_failure(page: Page):
    def handle_route(route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error": "Fake Error mene bnai hai"}',
        )
    page.route("https://jsonplaceholder.typicode.com/users/1", handle_route)

    page.goto("https://jsonplaceholder.typicode.com/users/1")
    
    expect(page.locator("body")).to_contain_text("Fake Error mene bnai hai")