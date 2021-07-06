from selenium import webdriver
from selenium_python_azure import Locators


driverLocation = Locators.DRIVER_Location
driver = webdriver.Chrome(driverLocation)
driver.get(Locators.URL)
driver.find_element_by_css_selector(Locators.CHOOSE_LANGUAGE).click()
for elem in driver.find_elements_by_css_selector(Locators.SELECT_ENGLISH):
    assert elem.text == Locators.ENGLISH_TEXT
for elem in driver.find_elements_by_css_selector(Locators.SELECT_DUTCH):
    assert  elem.text == Locators.DUTCH_TEXT
driver.find_element_by_css_selector(Locators.FULLNAME).send_keys(Locators.ENTER_NAME)
driver.find_element_by_css_selector(Locators.ORGANISATION).send_keys(Locators.ENTER_ORG)
driver.find_element_by_css_selector(Locators.EMAIL).send_keys(Locators.ENTER_EMAIL)
driver.find_element_by_css_selector(Locators.CHECKBOX).click()
driver.find_element_by_css_selector(Locators.BUTTON).click()