from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    # sleep(2)

    # 2 Send registered email to email field
    email_field = driver.find_element(*EML_FLD)
    email_field.clear()
    email_field.send_keys(email_valid)
    # sleep(2)

    # 3 Send valid password to password field
    passwrd_field = driver.find_element(*PSWRD_FLD)
    passwrd_field.clear()
    passwrd_field.send_keys(password_valid)
    # sleep(2)

    # 4 Click login button
    driver.find_element(*LGN_BTN).click()
    # sleep(2)

    # 5 Assert user is logged in
    registered_user_logged_logo = driver.find_element(*REGISTERED_USR_LOGGED_LOGO)
    expected_text = 'Viachesla...'
    actual_text = registered_user_logged_logo.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 6 Close the current instance
    sleep(2)
    driver.delete_all_cookies()
    driver.quit()





