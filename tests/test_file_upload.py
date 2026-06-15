import pytest


@pytest.mark.smoke
@pytest.mark.upload
def test_file_upload(file_upload_page):
    file_upload_page.open()

    file_upload_page.upload_file("sample_files/sample_upload.txt")
    file_upload_page.click_upload_button()

    file_upload_page.verify_upload_success_message()
    file_upload_page.verify_uploaded_file_name("sample_upload.txt")