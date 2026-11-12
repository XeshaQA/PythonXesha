import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



@pytest.mark.basic
def test_add_remove_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
    add_element.click()
    add_element.click()
    delete_elements = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

    assert len(delete_elements) == 2, 'There should be 2 elements detected.'

@pytest.mark.basic
def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    first_checkbox = checkboxes[0]
    second_checkbox = checkboxes[1]

    assert first_checkbox.is_selected() == False, "first checkbox shouldn't be selected"
    first_checkbox.click()
    assert first_checkbox.is_selected() == True, "first checkbox should be selected"

    assert second_checkbox.is_selected() == True, "second checkbox should be selected"
    second_checkbox.click()
    assert second_checkbox.is_selected() == False, "second checkbox shouldn't be selected"

@pytest.mark.basic
def test_dropdown(driver):

    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    all_options = select.options

    assert len(all_options) > 0, "dropdown is empty"

    select.select_by_value("1")

    selected_option = select.first_selected_option
    assert selected_option.text == "Option 1", "first option isn't selected"

    select.select_by_value("2")
    selected_option = select.first_selected_option
    assert selected_option.text == "Option 2", "second option isn't selected"

@pytest.mark.basic
def test_inputs(driver):
    driver.get("https://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.XPATH, "//input")

    input_field.send_keys('123')
    assert input_field.get_attribute("value") == "123", "can't write numbers"

    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys(Keys.BACKSPACE)

    input_field.send_keys("5")

    input_field.send_keys(Keys.ARROW_UP)

    assert input_field.get_attribute("value") == "6", "can't arrow up"

    input_field.send_keys(Keys.ARROW_DOWN)
    input_field.send_keys(Keys.ARROW_DOWN)

    assert input_field.get_attribute("value") == "4", "can't arrow down"

@pytest.mark.basic
def test_typos(driver):
    driver.get("https://the-internet.herokuapp.com/typos")

    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    paragraph_text = paragraphs[1].text

    assert "Sometimes you'll see a typo" in paragraph_text, 'Текст не совпадает'

    assert ("won't" in paragraph_text) or ("wont" in paragraph_text), f"Фактический результат не совпадает с ожидаемым. Фактический результат: {paragraph_text}"