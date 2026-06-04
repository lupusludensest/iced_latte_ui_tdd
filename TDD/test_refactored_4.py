from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def login_user(driver, email, password):
    driver.find_element(*USER_AUTH_ICON).click()
    sleep(4)
    email_field = driver.find_element(*EML_FLD)
    email_field.clear()
    email_field.send_keys(email)
    password_field = driver.find_element(*PSWRD_FLD)
    password_field.clear()
    password_field.send_keys(password)
    driver.find_element(*LGN_BTN).click()

def click_on_cart_icon(driver):
    driver.find_element(*CLCK_ON_CART_ICN).click()

def click_continue_shopping(driver):
    driver.find_element(*CNTNUE_SHPNG_BTN).click()

def add_turkish_coffee_to_cart(driver):
    driver.find_element(*ADD_TRKSH_CFFE).click()

def click_on_cart_icon_after_adding(driver):
    driver.find_element(*CRT_BTN_AFTR_ADDING).click()

def verify_coffee_in_cart(driver):
    # Counter "1" is here
    cntr_1_is_here = driver.find_element(*CNTR_1_HERE)
    expected_text = '1'
    actual_text = cntr_1_is_here.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # Text "Turkish Coffee" is in the cart
    trksh_cff_in_the_cart = driver.find_element(*TRKSH_CFF_IN_THE_CRT)
    expected_text = 'Turkish Coffee'
    actual_text = trksh_cff_in_the_cart.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # Text "500 g." is in the cart
    five_hndrd_grms_txt = driver.find_element(*FIVE_HNDRD_GRMS_TXT)
    expected_text = '500 g.'
    actual_text = five_hndrd_grms_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # Text "$4.49" is in the cart
    four_forty_nine_dlrs_txt = driver.find_element(*FOUR_HUNDRED_FORTY_NINE_DLRS)
    expected_text = '$4.49'
    actual_text = four_forty_nine_dlrs_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

def go_to_checkout(driver):
    go_to_chck_out_btn = driver.find_element(*GO_TO_CHCK_OUT_BTN)
    expected_text = 'Go to checkout'
    actual_text = go_to_chck_out_btn.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

def test_iced_latte_ui_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://iced-latte.uk/")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    email_valid = 'gurovvic@gmail.com'
    password_valid = 'qwertyuiop12!@'

    login_user(driver, email_valid, password_valid)
    click_on_cart_icon(driver)
    click_continue_shopping(driver)
    add_turkish_coffee_to_cart(driver)
    click_on_cart_icon_after_adding(driver)
    verify_coffee_in_cart(driver)
    go_to_checkout(driver)

    driver.delete_all_cookies()
    driver.quit()