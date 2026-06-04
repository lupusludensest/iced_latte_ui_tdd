from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    # sleep(2)

    # 2 Click user registration button
    driver.find_element(*REGISTER_BTN).click()
    # sleep(2)

    # 3 Send first name to first name field
    first_name_field = driver.find_element(*FRST_NM_FLD)
    first_name_field.clear()
    first_name_field.send_keys(first_name)
    # sleep(2)

    # 4 Send last name to last name field
    last_name_field = driver.find_element(*LST_NM_FLD)
    last_name_field.clear()
    last_name_field.send_keys(last_name)
    # sleep(2)

    # 5 Send email to email field
    email_field = driver.find_element(*EML_FLD)
    email_field.clear()
    email_field.send_keys(email_valid)
    # sleep(2)

    # 6 Send password to password field
    password_field = driver.find_element(*PSWRD_FLD)
    password_field.clear()
    password_field.send_keys(password_valid)
    # sleep(2)

    # 7 Click user register user button
    driver.find_element(*REGISTER_USER_BTN).click()
    # sleep(2)

    # 8 Close the current instance
    sleep(2)
    driver.delete_all_cookies()
    driver.quit()