from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from ..utils import helper
from ..utils import custom_logger
import string
import random
import time

logger_helper = custom_logger.LoggerHelper()
Logger = logger_helper.json_logger()


class Screen(object):
    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_until_element_visible(self, by, locator, wait=3):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.visibility_of_element_located((by, locator))
            )
            if element:
                Logger.info("Element {0} Found".format(locator))
                return True
            else:
                Logger.warning("Element {0} NOT Found".format(locator))
                return False
        except TimeoutException:
            Logger.warning("Element {0} Not Found".format(locator))
            return False

    def wait_until_element_not_visible(self, by, locator, wait=3):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.invisibility_of_element_located((by, locator))
            )
            if element:
                return True
        except TimeoutException as e:
            print(e)
            return False

    def click_element(self, by, locator, wait=5):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.element_to_be_clickable((by, locator))
            )

            element.click()
            Logger.info('Click Element {0}'.format(locator))
            return True
        except (NoSuchElementException, WebDriverException, TimeoutException):
            Logger.warning('Click Element %s is fail' % locator)
            return False

    def click_element_javascript(self, by, locator):
        by = helper.method_by(by)
        try:
            element = self.driver.find_element(by, locator)
            self.driver.execute_script("arguments[0].click();", element)

        except(NoSuchElementException, WebDriverException, TimeoutException):
            Logger.warning('Click Element %s is fail' % locator)
            return False

    def get_element(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except NoSuchElementException:
            Logger.warning("No such element")
            return None

    def clear_field(self, by, locator):
        element = self.find_elements(by, locator)
        if element:
            Logger.info("Clearing text field" + locator)
            element.clear()
            return True
        else:
            return False

    def find_elements(self, by: str, locator: str, wait=4):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, int(wait)).until(
                EC.visibility_of_element_located((by, locator))
            )
            Logger.info("Element " + locator + " Found")
            return element
        except TimeoutException:
            Logger.warning("Find_Elements {0} has reached Timeout Exception".format(locator))
            return None

    def find_element_and_input_javascript(self, by: str, locator: str, wait: int, text: str):
        element = self.find_elements(by, locator, wait)
        if element:
            self.driver.execute_script("arguments[0].setAttribute('value','" + text + "')", element)
            return True
        else:
            return False

    def find_element_and_input(self, by: str, locator: str, wait: int, text: str):
        element = self.find_elements(by, locator, wait)

        if element:
            time.sleep(2)
            Logger.info("Sending text " + text + "to the " + locator)
            element.send_keys(text)
            return True
        else:
            return False


def find_element_and_send_code(self, *code):
    self.driver.press_keycode(code)


def send_value(self, element, value):
    self.driver.set_value(element, value)
    return True


def swipe_up_until_element_visible(self, scroll_element, by, locator_to_find, how_many_scroll):
    element = self.wait_until_element_visible(by, locator_to_find)
    time = 0
    while not element and time != how_many_scroll:
        self.swipe_up(scroll_element)
        element = self.wait_until_element_visible(by, locator_to_find)
        time += 1


def swipe_up(self, element=''):
    if not element or element == '':
        element = self._default_element()
    element_size = element.size
    element_location = element.location
    x = element_location['x']
    y = element_location['y']
    width = element_size['width']
    height = element_size['height']
    start_x = x + (width * 0.5)
    start_y = y + (height * 0.7)
    end_x = x + (width * 0.5)
    end_y = y + (height * 0.3)
    return self.driver.swipe(start_x, start_y, end_x, end_y, 1000)


def swipe_down(self, element):
    element_size = element.size()
    element_location = element.location()
    x = element_location['x'], y = element_location['y']
    width = element_size['width'], height = element_size['height']
    start_x = x + (width * 0.5)
    start_y = y + (height * 0.3)
    end_x = x + (width * 0.5)
    end_y = y + (height * 0.7)
    return self.driver.swipe(start_x, start_y, end_x, end_y, 1000)


def swipe_left(self, element):
    element_size = element.size()
    element_location = element.location()
    x = element_location['x'], y = element_location['y']
    width = element_size['width'], height = element_size['height']
    start_x = x + (width * 0.85)
    start_y = y + (height * 0.5)
    end_x = x + (width * 0.15)
    end_y = y + (height * 0.5)
    return self.driver.swipe(start_x, start_y, end_x, end_y, 500)


def swipe_right(self, element):
    element_size = element.size()
    element_location = element.location()
    x = element_location['x'], y = element_location['y']
    width = element_size['width'], height = element_size['height']
    start_x = x + (width * 0.15)
    start_y = y + (height * 0.5)
    end_x = x + (width * 0.85)
    end_y = y + (height * 0.5)
    return self.driver.swipe(start_x, start_y, end_x, end_y, 500)


class ActionHelper:
    def __init__(self, driver: Remote):
        self.driver = driver
        self.screen = Screen(driver)

    def action(self, **kwargs):
        by = kwargs.get('by')
        text = kwargs.get('text')
        timeout = kwargs.get('wait')
        action = kwargs.get('action')
        locator = kwargs.get('locator')

        if not timeout:
            timeout = 5
        elif timeout:
            timeout = int(timeout)

        if text == 'Random':
            return 'C' + ''.join(random.choice(string.digits) for _ in range(6))
        if action == "wait":
            return self.wait(by, locator, timeout)
        elif action == "click":
            return self.click(by, locator, timeout)
        elif action == "click_yogrt":
            return self.click_yogrt(by, locator, timeout)
        elif action == "click_javascript":
            return self.click_javascript(by, locator)
        elif action == 'scroll' or action == 'swipe':
            return self.scroll_down()
        elif action == 'scrollDown':
            return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elif action == "click_if_displayed":
            return self.click(by, locator, timeout)
        elif action == "navigate_back":
            self.driver.back()
            return True
        elif action == "input_javascript":
            return self.find_and_input_javascript(by, locator, timeout, text)
        elif action == "input":
            return self.find_and_input(by, locator, timeout, text)
        elif action == "sleep":
            time.sleep(5)
            return True
        elif action == "press_code":
            # TODO
            pass

        else:
            Logger.warning(action)
            raise NameError

    def wait(self, by: str, locator: str, wait=5):
        return self.screen.wait_until_element_visible(by, locator, wait)

    def click(self, by: str, locator: str, wait=5):
        return self.screen.click_element(by, locator, wait)

    def click_javascript(self, by: str, locator: str):
        return self.screen.click_element_javascript(by, locator)

    def find_and_input(self, by, locator, wait, text):
        return self.screen.find_element_and_input(by, locator, wait, text)

    def find_and_input_javascript(self, by, locator, wait, text):
        return self.screen.find_element_and_input_javascript(by, locator, wait, text)
