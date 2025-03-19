from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SECOND_PAGE_BUTTON = (By.XPATH, "//a[@aria-label='2 sayfasına git']")
    SELECTED_PAGE = (By.CSS_SELECTOR, ".s-pagination-selected")
    THIRD_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result'])[3]//h2")

    def go_to_second_page(self):
        second_page = self.wait_for_element_to_be_clickable(self.SECOND_PAGE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", second_page)
        second_page.click()

    def is_on_second_page(self):
        selected_page = self.wait_for_element(self.SELECTED_PAGE)
        return selected_page.text.strip() == "2"

    def select_third_product(self):
        third_product = self.wait_for_element_to_be_clickable(self.THIRD_PRODUCT)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", third_product)
        third_product.click()
