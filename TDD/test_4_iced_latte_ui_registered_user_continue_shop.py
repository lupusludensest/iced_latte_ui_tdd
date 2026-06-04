from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    sleep(2)

    # 2 Send registered email to email field
    first_name_field = driver.find_element(*EML_FLD)
    first_name_field.clear()
    first_name_field.send_keys(email_valid)
    # sleep(2)

    # 3 Send valid password to password field
    first_name_field = driver.find_element(*PSWRD_FLD)
    first_name_field.clear()
    first_name_field.send_keys(password_valid)
    # sleep(2)

    # 4 Click login button
    driver.find_element(*LGN_BTN).click()
    # sleep(2)

    # 5 Click on cart icon
    driver.find_element(*CLCK_ON_CART_ICN).click()
    # sleep(2)

    # 6 Click on Continue Shopping button
    driver.find_element(*CNTNUE_SHPNG_BTN).click()
    # sleep(2)

    # 7 Click on "+" button, adding Turkish Coffee to the cart
    driver.find_element(*ADD_TRKSH_CFFE).click()
    # sleep(2)

    # 8 Click on cart icon after adding
    driver.find_element(*CRT_BTN_AFTR_ADDING).click()
    # sleep(2)

    # 9 Verify the coffee is in the cart

    # 9.1 Counter "1" is here
    cntr_1_is_here = driver.find_element(*CNTR_1_HERE)
    expected_text = '1'
    actual_text = cntr_1_is_here.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.2 Text "Turkish Coffee" is in the page in cart
    trksh_cff_in_the_cart = driver.find_element(*TRKSH_CFF_IN_THE_CRT)
    expected_text = 'Turkish Coffee'
    actual_text = trksh_cff_in_the_cart.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.3 Text "500 g." is in the page in cart
    five_hndrd_grms_txt = driver.find_element(*FIVE_HNDRD_GRMS_TXT)
    expected_text = '500 g.'
    actual_text = five_hndrd_grms_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.4 Text "$4.49" is in the page in cart $4.49
    four_forty_nine_dlrs_txt = driver.find_element(*FOUR_HUNDRED_FORTY_NINE_DLRS)
    expected_text = '$4.49'
    actual_text = four_forty_nine_dlrs_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 10 Button "Go to checkout" is here
    go_to_chck_out_btn = driver.find_element(*GO_TO_CHCK_OUT_BTN)
    expected_text = 'Go to checkout'
    actual_text = go_to_chck_out_btn.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 11 Close the current instance
    sleep(2)
    driver.delete_all_cookies()
    driver.quit()