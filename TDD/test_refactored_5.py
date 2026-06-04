from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def reset_password(driver, email, code, new_password):
    driver.find_element(*USER_AUTH_ICON).click()
    sleep(4)
    driver.find_element(*FRGT_PSSWD).click()
    sleep(4)
    email_field = driver.find_element(*ENTR_YR_EML_ADDRSS_FLD_RST_PSWD)
    email_field.clear()
    email_field.send_keys(email)
    driver.find_element(*SND_RST_LNK).click()
    sleep(4)
    driver.find_element(*CNTNUE_TO_CNHG_YR_PSWRD).click()
    sleep(4)
    code_field = driver.find_element(*CODE_FROM_EMAIL_FLD)
    code_field.clear()
    code_field.send_keys(code)
    new_password_field = driver.find_element(*NEW_PASSWORD_FLD)
    new_password_field.clear()
    new_password_field.send_keys(new_password)
    confirm_password_field = driver.find_element(*CNFRM_YR_PSWRD_FLD)
    confirm_password_field.clear()
    confirm_password_field.send_keys(new_password)
    driver.find_element(*RESET_PSWRD_BTN).click()
    sleep(4)
    incorrect_token_text = driver.find_element(*INCORRECT_TOKEN_TEXT)
    expected_text = 'Server Error: Incorrect token'
    actual_text = incorrect_token_text.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

def test_iced_latte_ui_5():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    email_valid = 'gurovvic@gmail.com'
    code = '861-539-280'
    new_password = 'asdfghjkl12!@'

    reset_password(driver, email_valid, code, new_password)

    sleep(4)
    driver.delete_all_cookies()
    driver.quit()