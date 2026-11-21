import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.advanced
def test_dynamic_control(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")

    browser.find_element(By.XPATH, "//button[text()='Remove']").click()

    wait = WebDriverWait(browser, 10)

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))

    assert message.text == "It's gone!"

    checkboxes = browser.find_elements(By.ID, "checkbox")
    assert len(checkboxes) == 0

    input_field = browser.find_element(By.CSS_SELECTOR, "#input-example input")
    assert not input_field.is_enabled()

    browser.find_element(By.XPATH, "//button[text()='Enable']").click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's enabled!"))

    assert input_field.is_enabled()