import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_setup import get_driver

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://www.demoblaze.com/")
    
    def tearDown(self):
        self.driver.quit()

    def test_login_positive(self):
        driver = self.driver
        wait = self.wait

        # Perform login with valid credentials
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        driver.find_element(By.ID, "loginusername").send_keys("yk@gmail.com")
        driver.find_element(By.ID, "loginpassword").send_keys("Yk@123")
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Validate successful login
        try:
            # Check if the logout button is visible to confirm successful login
            wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
            self.assertTrue(driver.find_element(By.ID, "logout2").is_displayed(), "Login was not successful.")
            
            # Log out after successful login
            driver.find_element(By.ID, "logout2").click()
            
            # Confirm logout by checking that login button is visible again
            wait.until(EC.visibility_of_element_located((By.ID, "login2")))
            self.assertTrue(driver.find_element(By.ID, "login2").is_displayed(), "Logout was not successful.")
        except Exception as e:
            self.fail(f"Login positive test failed with exception: {e}")

    def test_login_negative(self):
        driver = self.driver
        wait = self.wait

        # Perform login with invalid credentials
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        driver.find_element(By.ID, "loginusername").send_keys("invalid_user")
        driver.find_element(By.ID, "loginpassword").send_keys("wrong_password")
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Validate failure
        try:
            alert = wait.until(EC.alert_is_present())
            self.assertEqual(alert.text, "Wrong password.", "Alert text did not match the expected 'Wrong password.'")
            alert.accept()
        except Exception as e:
            self.fail(f"Login negative test failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
