from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def close_cookies(self):
        try:
            accept_cookies_button = self.wait_for_element_to_be_clickable(('id', 'sp-cc-accept'), timeout=5)
            accept_cookies_button.click()
            print("Cookies closed.")
        except TimeoutException:
            print("No cookies notification found, proceeding.")
