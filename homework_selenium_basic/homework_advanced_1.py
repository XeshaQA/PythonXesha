import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.advanced
def test_context_menu(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")

    hotspot = browser.find_element(By.ID, "hot-spot")

    actions = ActionChains(browser)
    actions.context_click(hotspot).perform()

    wait = WebDriverWait(browser, 5)
    alert = wait.until(EC.alert_is_present())

    assert alert.text == "You selected a context menu", f"Несоответствие ожидаемому результату"

    alert.dismiss()