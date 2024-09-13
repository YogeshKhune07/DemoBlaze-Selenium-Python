import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_setup import get_driver

class TestProductBrowsing(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 60)

    def tearDown(self):
        self.driver.quit()

    def test_products_displayed_on_homepage(self):
        driver = self.driver
        wait = self.wait

        try:
            # Wait until products are loaded on the homepage
            products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "card")))

            # Verify products are displayed on the homepage
            if products:
                print(f"{len(products)} products displayed on the homepage.")
                self.assertGreater(len(products), 0, "No products are displayed on the homepage.")
            else:
                self.fail("No products found on the homepage.")
        except Exception as e:
            self.fail(f"Exception occurred while verifying products on homepage: {e}")

    def test_product_categories_navigation(self):
        driver = self.driver
        wait = self.wait

        try:
            # Get a list of categories on the homepage
            categories = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#itemc")))

            # Verify that categories are displayed
            if categories:
                print(f"{len(categories)} categories available for navigation.")
                self.assertGreater(len(categories), 0, "No categories are available for navigation.")

                # Navigate through each category and verify products load
                for category in categories:
                    category_name = category.text
                    print(f"Navigating to category: {category_name}")

                    # Click on the category
                    category.click()

                    # Wait for the products to load under the selected category
                    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card")))

                    # Verify that products are displayed for the selected category
                    products_in_category = driver.find_elements(By.CLASS_NAME, "card")
                    self.assertGreater(len(products_in_category), 0, f"No products found under category {category_name}.")
                    print(f"{len(products_in_category)} products displayed under {category_name} category.")
            else:
                self.fail("No categories found on the homepage.")
        except Exception as e:
            self.fail(f"Exception occurred while navigating through categories: {e}")

if __name__ == "__main__":
    unittest.main()
