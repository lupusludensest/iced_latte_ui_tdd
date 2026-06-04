from all_locators_tdd import *
from credentials import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def test_iced_latte_ui_6():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    click_heart_icon(driver)
    click_continue_shopping_button(driver)
    click_heart_icon_on_vanilla_latte(driver)
    click_heart_icon_on_turkish_coffee(driver)
    click_heart_icon_again(driver)
    verify_text_in_the_cart(driver, TRKSH_CFF_IN_THE_CRT, 'Turkish Coffee')
    verify_text_in_the_cart(driver, FOUR_POINT_FOURTY_NINE_DOLLARS, '$4.49')
    verify_text_in_the_cart(driver, VANILLA_LATTE_TEXT, 'Vanilla Latte')
    verify_text_in_the_cart(driver, FOUR_POINT_EIGTHY_FIVE_DOLLARS, '$4.85')

    sleep(2)
    driver.delete_all_cookies()
    driver.quit()

def click_heart_icon(driver):
    driver.find_element(*HEART_ICON_FAVORITIES).click()

def click_continue_shopping_button(driver):
    driver.find_element(*CNTNUE_SHPNG_BTN).click()

def click_heart_icon_on_vanilla_latte(driver):
    driver.find_element(*HEART_VANILLA_LATTE).click()

def click_heart_icon_on_turkish_coffee(driver):
    driver.find_element(*HEART_TURKISH_COFFEE).click()

def click_heart_icon_again(driver):
    driver.find_element(*HEART_ICON_FAVORITIES).click()

def verify_text_in_the_cart(driver, locator, expected_text):
    element_text = driver.find_element(*locator).text
    assert element_text == expected_text, f'Expected {expected_text}, but got {element_text}'