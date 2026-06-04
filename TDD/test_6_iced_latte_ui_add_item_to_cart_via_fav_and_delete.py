from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_6():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click Heart icon
    driver.find_element(*HEART_ICON_FAVORITIES).click()
    # sleep(2)

    # 2 Click on Continue Shopping button
    driver.find_element(*CNTNUE_SHPNG_BTN).click()
    # sleep(2)

    # 3 Click on Heart icon on Vanilla Latte
    driver.find_element(*HEART_VANILLA_LATTE).click()
    # sleep(2)

    # 4 Click on Heart icon on Turkish Coffee
    driver.find_element(*HEART_TURKISH_COFFEE).click()
    # sleep(2)

    # 5 Click Heart icon again
    driver.find_element(*HEART_ICON_FAVORITIES).click()
    # sleep(2)

    # 6 Verify Turkish Coffee text is here
    turkish_coffee_text = driver.find_element(*TRKSH_CFF_IN_THE_CRT)
    expected_text = 'Turkish Coffee'
    actual_text = turkish_coffee_text.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 7 Text "$4.49" is in the page in cart $4.49
    four_forty_nine_dlrs_txt = driver.find_element(*FOUR_POINT_FOURTY_NINE_DOLLARS)
    expected_text = '$4.49'
    actual_text = four_forty_nine_dlrs_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 8 Verify Vanilla Latte text is here
    vanilla_coffee_text = driver.find_element(*VANILLA_LATTE_TEXT)
    expected_text = 'Vanilla Latte'
    actual_text = vanilla_coffee_text.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9 Text "$4.85" is in the page in cart $4.49
    four_eigthy_five_dlrs_txt = driver.find_element(*FOUR_POINT_EIGTHY_FIVE_DOLLARS)
    expected_text = '$4.85'
    actual_text = four_eigthy_five_dlrs_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 10 Close the current instance
    sleep(2)
    driver.delete_all_cookies()
    driver.quit()
