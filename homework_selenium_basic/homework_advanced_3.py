import pytest
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.advanced
def test_file_upload(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    browser.maximize_window()

    wait = WebDriverWait(browser, 10)
    file_path = Path(__file__).parent / "upload.txt"

    browser.find_element(By.ID, "file-upload").send_keys(str(file_path.resolve()))
    browser.find_element(By.ID, "file-submit").click()

    uploaded = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))

    assert uploaded.text == file_path.name