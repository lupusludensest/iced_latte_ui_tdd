from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def log_in_registered_user(driver, email, password):
    driver.find_element(*USER_AUTH_ICON).click()
    sleep(4)

    email_field = driver.find_element(*EML_FLD)
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element(*PSWRD_FLD)
    password_field.clear()
    password_field.send_keys(password)

    driver.find_element(*LGN_BTN).click()

def assert_user_logged_in(driver, expected_text):
    registered_user_logged_logo = driver.find_element(*REGISTERED_USR_LOGGED_LOGO)
    actual_text = registered_user_logged_logo.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

def test_iced_latte_ui_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://iced-latte.uk/")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    email_valid = 'gurovvic@gmail.com'
    password_valid = 'qwertyuiop12!@'

    log_in_registered_user(driver, email_valid, password_valid)
    sleep(2)

    expected_text = 'Viachesla...'
    assert_user_logged_in(driver, expected_text)

    driver.delete_all_cookies()
    driver.quit()