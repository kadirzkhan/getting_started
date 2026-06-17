from pathlib import Path
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


def test_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")

    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)

    with page.expect_download() as download_info:
        page.locator(".example a").nth(1).click()

    download = download_info.value

    downloaded_file_path = downloads_dir / download.suggested_filename
    download.save_as(downloaded_file_path)

    assert downloaded_file_path.exists()
    assert downloaded_file_path.name == download.suggested_filename