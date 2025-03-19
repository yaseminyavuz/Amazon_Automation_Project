from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_BUTTON = (By.XPATH, "//*[@id='sw-gtc']/span/a")

    def add_to_cart(self):
        add_to_cart_button = self.wait_for_element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_button = self.wait_for_element_to_be_clickable(self.CART_BUTTON)
        cart_button.click()
