from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_python_azure import Locators

driverLocation = Locators.DRIVER_Location
driver = webdriver.Chrome(driverLocation)
driver.get(Locators.GMAIL_URL)
driver.find_element_by_css_selector(Locators.GMAIL_EMAIL).send_keys(Locators.ENTER_EMAIL)
driver.find_element_by_css_selector(Locators.NEXT_EMAIL).click()
driver.implicitly_wait(500)
driver.find_element_by_css_selector(Locators.PWD).send_keys(Locators.ENTER_PWD)
driver.find_element_by_css_selector(Locators.PWD_NEXT).click()
driver.implicitly_wait(1000)
driver.get(Locators.SIGNED_URL)
driver.find_element_by_link_text(Locators.SIGN_IN).click()
driver.find_element_by_css_selector(Locators.CLICK_EMAIL).click()
driver.implicitly_wait(200)
driver.find_element_by_css_selector(Locators.PROMOTIONS).click()
driver.implicitly_wait(200)
driver.find_element_by_xpath(Locators.RECEIVED_EMAIL).click()


