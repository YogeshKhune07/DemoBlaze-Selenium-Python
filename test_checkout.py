import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_setup import get_driver

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 60)
    
    def tearDown(self):
        self.driver.quit()

    def add_product_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Wait until the product grid is loaded
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card")))

        # Click on the first product to view details
        product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hrefch")))
        product_name = product.text
        print(f"Adding product: {product_name} to cart")
        product.click()

        # Wait for the product page to load and add the product to the cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success.btn-lg"))).click()

        # Handle the alert for product added to cart
        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept()  # Accept the alert
            print(f"Product '{product_name}' added to cart successfully.")
        except Exception as e:
            self.fail(f"Unexpected alert present: {e}")

    def wait_for_purchase_and_click(self):
        """Wait until the 'Purchase' button is visible and clickable, then click."""
        try:
            # Using XPath with the 'onclick' attribute to locate the button
            purchase_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='purchaseOrder()']")))
            print("Purchase button is visible and clickable.")
            purchase_button.click()
            print("Clicked on Purchase button.")
        except Exception as e:
            self.fail(f"Purchase button not found or not clickable: {e}")

    def fill_checkout_form(self, name="abcd", country="Country", city="City", card="123456", month="Month", year="Year"):
        """Fill the checkout form with given or default values."""
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.ID, "country"))).send_keys(country)
        wait.until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(city)
        wait.until(EC.element_to_be_clickable((By.ID, "card"))).send_keys(card)
        wait.until(EC.element_to_be_clickable((By.ID, "month"))).send_keys(month)
        wait.until(EC.element_to_be_clickable((By.ID, "year"))).send_keys(year)

    def verify_order_success(self):
        """Verify that the order was placed successfully by checking the success message."""
        try:
            success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sweet-alert"))).text
            self.assertIn("Thank you for your purchase!", success_message)
            print("Order placed successfully.")
            print(f"Order details: {success_message}")
        except Exception as e:
            self.fail(f"Confirmation message not found: {e}")

    def checkout_with_incomplete_info(self):
        """Proceed with checkout using incomplete information."""
        driver = self.driver
        wait = self.wait

        # Navigate to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()

        # Proceed with checkout
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success"))).click()

        # Fill out the checkout form with incomplete information
        self.fill_checkout_form()

        # Wait for the purchase button and click it
        self.wait_for_purchase_and_click()

        # Verify the confirmation message
        self.verify_order_success()

    def test_checkout_with_items(self):
        """Test the checkout process with items in the cart."""
        self.add_product_to_cart()
        self.checkout_with_incomplete_info()

    def test_checkout_with_empty_cart(self):
        """Test the checkout process with an empty cart."""
        driver = self.driver
        wait = self.wait

        # Navigate to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()

        # Check if the cart is empty
        cart_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))
        cart_rows = cart_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        
        if len(cart_rows) == 0:
            print("Cart is empty. Proceeding with checkout.")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success"))).click()

            # Fill out the checkout form with incomplete information
            self.fill_checkout_form()

            # Wait for the purchase button and click it
            self.wait_for_purchase_and_click()

            # Verify the confirmation message
            self.verify_order_success()
        else:
            self.fail("Cart is not empty, which is not expected for this test.")

if __name__ == "__main__":
    unittest.main()
