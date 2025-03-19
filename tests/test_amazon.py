import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


from pages.product_page import ProductPage
from pages.cart_page import CartPage


class AmazonTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

    def test_amazon_flow(self):
        home_page = HomePage(self.driver)
        home_page.search_for_item("samsung")

        search_results = SearchResultsPage(self.driver)
        search_results.go_to_second_page()
        self.assertTrue(search_results.is_on_second_page())
        search_results.select_third_product()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.delete_product_from_cart()

        home_page.click_amazon_logo()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
