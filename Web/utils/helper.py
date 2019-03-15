from selenium import webdriver as normalDriver
from selenium.webdriver.common.by import By
from .custom_logger import LoggerHelper
from .config import Get
import random

custom_logger = LoggerHelper.json_logger()


def method_by(by: str):
    if by == 'accessibility_id':
        return By.ACCESSIBILITY_ID
    elif by == 'class_name':
        return By.CLASS_NAME
    elif by == 'id':
        return By.ID
    elif by == 'xpath':
        return By.XPATH
    elif by == 'name':
        return By.NAME
    elif 'css' in by:
        return By.CSS_SELECTOR
    else:
        raise Exception('Invalid locator method.')


def open_browser_connect(url):
    driver = normalDriver.Chrome(Get.chrome_driver())
    driver.get(url)
    return driver


def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length, 2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


def close_application(driver: normalDriver.Remote):
    driver.close_app()


def quit_driver(driver: normalDriver.Remote):
    driver.quit()


def close_driver(driver):
    driver.quit()
