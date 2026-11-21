import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.advanced
def test_frames(browser):
    browser.get("https://the-internet.herokuapp.com/iframe")
    browser.maximize_window()

    iframe = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe)

    text_element = browser.find_element(By.XPATH, "//body[@id='tinymce']//p")
    assert text_element.text == "Your content goes here."