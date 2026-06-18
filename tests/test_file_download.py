from pathlib import Path
import pytest
from playwright.sync_api import Page


@pytest.mark.smoke
@pytest.mark.download
def test_file_download(page: Page, browser_name):
    if browser_name == "webkit":
        pytest.skip("Skipping file download test on WebKit because demo site opens some files instead of firing download event.")

    page.goto("https://the-internet.herokuapp.com/download")

    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)

    links = page.locator(".example a")
    count = links.count()

    for index in range(count):
        link = links.nth(index)
        file_name = link.inner_text().strip()

        if "[" not in file_name and "]" not in file_name:
            with page.expect_download() as download_info:
                link.click()

            download = download_info.value
            downloaded_file_path = downloads_dir / download.suggested_filename
            download.save_as(downloaded_file_path)

            assert downloaded_file_path.exists()
            assert downloaded_file_path.name == download.suggested_filename
            return

    raise Exception("No safe downloadable file found")