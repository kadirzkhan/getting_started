from pathlib import Path
from playwright.sync_api import Page
from pages.base_page import BasePage


class FileUploadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.success_message = page.locator("h3")
        self.uploaded_file_name = page.locator("#uploaded-files")

    def open(self):
        self.open_url("https://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path: str):
        full_file_path = Path(file_path).resolve()
        self.file_input.set_input_files(str(full_file_path))

    def click_upload_button(self):
        self.click_element(self.upload_button)

    def verify_upload_success_message(self):
        self.verify_text(self.success_message, "File Uploaded!")

    def verify_uploaded_file_name(self, expected_file_name: str):
        self.verify_text(self.uploaded_file_name, expected_file_name)