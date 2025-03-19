from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    AMAZON_LOGO = (By.XPATH, "//a[@id='nav-logo-sprites']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com.tr")
        self.close_cookies()

    def search_for_item(self, item):
        self.wait_for_element_to_be_clickable(self.SEARCH_BOX).send_keys(item)
        self.wait_for_element_to_be_clickable(self.SEARCH_BUTTON).click()
        print(f"Search initiated for '{item}'.")

    def click_amazon_logo(self):
        logo = self.wait_for_element_to_be_clickable(self.AMAZON_LOGO)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", logo)
        logo.click()
        print("Returned to home page.")
