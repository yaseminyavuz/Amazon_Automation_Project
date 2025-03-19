from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    DELETE_BUTTON = (By.XPATH, "//input[contains(@name, 'submit.delete')]")

    def delete_product_from_cart(self):
        delete_button = self.wait_for_element_to_be_clickable(self.DELETE_BUTTON)
        delete_button.click()
