import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_setup import get_driver
import random
import string

class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 30)  # Set up WebDriverWait
    
    def tearDown(self):
        self.driver.quit()

    def generate_unique_username(self):
        """Generate a unique username using a random string."""
        return "user" + ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@example.com"

    def test_signup_positive(self):
        driver = self.driver
        wait = self.wait

        username = self.generate_unique_username()
        password = "newPassword1234"

        # Open the Sign-up modal
        wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

        # Wait for modal to fully load
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))

        # Input valid credentials
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the 'Sign up' button
        signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
        signup_button.click()

        # Handle success or error scenarios
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")  # Debugging line
            if "Sign up successful." in alert_text:
                self.assertEqual(alert_text, "Sign up successful.", "Sign-up was not successful.")
            elif "This user already exist." in alert_text:
                self.fail("Sign-up failed because user already exists. Consider using a unique username.")
            elif "Please fill out Username and Password." in alert_text:
                self.fail("Sign-up failed due to empty fields. This should not happen with valid inputs.")
            else:
                self.fail(f"Unexpected alert message: {alert_text}")
            alert.accept()
        except Exception as e:
            self.fail(f"Sign-up process failed with exception: {e}")

    def test_signup_negative(self):
        driver = self.driver
        wait = self.wait

        # Open the Sign-up modal
        wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

        # Wait for modal to fully load
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))

        # Input invalid credentials (empty fields)
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

        username_field.send_keys("")  # Empty username
        password_field.send_keys("")  # Empty password

        # Click the 'Sign up' button
        signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
        signup_button.click()

        # Handle failure via alert
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")  # Debugging line
            self.assertEqual(alert_text, "Please fill out Username and Password.", "Unexpected error message for invalid sign-up.")
            alert.accept()
        except Exception as e:
            self.fail(f"Sign-up process failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
