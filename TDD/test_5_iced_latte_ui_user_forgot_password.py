from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_5():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    # sleep(2)

    # 2 Click on Forgot password button
    driver.find_element(*FRGT_PSSWD).click()
    # sleep(2)

    # 3 Send email to email field to reset password
    first_name_field = driver.find_element(*ENTR_YR_EML_ADDRSS_FLD_RST_PSWD)
    first_name_field.clear()
    first_name_field.send_keys(email_valid)
    # sleep(2)

    # 4 Click on Send reset link button
    driver.find_element(*SND_RST_LNK).click()
    # sleep(2)

    # 5 Click on Continue to change your password button
    driver.find_element(*CNTNUE_TO_CNHG_YR_PSWRD).click()
    # sleep(2)

    # 6 Send code from email to the field
    code_from_email_field = driver.find_element(*CODE_FROM_EMAIL_FLD)
    code_from_email_field.clear()
    code_from_email_field.send_keys('861-539-280')
    # sleep(2)

    # 7 Send new password to the filed
    new_password_field = driver.find_element(*NEW_PASSWORD_FLD)
    new_password_field.clear()
    new_password_field.send_keys('asdfghjkl12!@')
    # sleep(2)

    # 8 Send new password confirmation to the filed
    new_password_confirmation_field = driver.find_element(*CNFRM_YR_PSWRD_FLD)
    new_password_confirmation_field.clear()
    new_password_confirmation_field.send_keys('asdfghjkl12!@')
    # sleep(2)

    # 9 Click on Reset password button
    driver.find_element(*RESET_PSWRD_BTN).click()
    # sleep(2)

    # 10 Verify message "Server Error: Incorrect token" is here
    incorrect_token_text = driver.find_element(*INCORRECT_TOKEN_TEXT)
    expected_text = 'Server Error: Incorrect token'
    actual_text = incorrect_token_text.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 11 Close the current instance
    sleep(4)
    driver.delete_all_cookies()
    # driver.quit()