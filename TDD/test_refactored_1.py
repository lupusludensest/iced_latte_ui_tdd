from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def click_user_auth_icon(driver):
    driver.find_element(*USER_AUTH_ICON).click()

def click_user_registration_button(driver):
    driver.find_element(*REGISTER_BTN).click()

def send_first_name(driver, first_name):
    first_name_field = driver.find_element(*FRST_NM_FLD)
    first_name_field.clear()
    first_name_field.send_keys(first_name)

def send_last_name(driver, last_name):
    last_name_field = driver.find_element(*LST_NM_FLD)
    last_name_field.clear()
    last_name_field.send_keys(last_name)

def send_email(driver, email):
    email_field = driver.find_element(*EML_FLD)
    email_field.clear()
    email_field.send_keys(email)

def send_password(driver, password):
    password_field = driver.find_element(*PSWRD_FLD)
    password_field.clear()
    password_field.send_keys(password)

def click_register_user_button(driver):
    driver.find_element(*REGISTER_USER_BTN).click()

def test_iced_latte_ui_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://iced-latte.uk/")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    click_user_auth_icon(driver)
    sleep(2)

    click_user_registration_button(driver)
    sleep(2)

    send_first_name(driver, 'Viacheslav')
    sleep(2)

    send_last_name(driver, 'Gurov')
    sleep(2)

    send_email(driver, 'gurovvic@gmail.com')
    sleep(2)

    send_password(driver, 'qwertyuiop12!@')
    sleep(2)

    click_register_user_button(driver)
    sleep(2)

    driver.delete_all_cookies()
    driver.quit()