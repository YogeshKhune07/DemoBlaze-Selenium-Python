from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")  # Start with maximized window

    service = Service('C:\\Selenium_proj\\chromedriver.exe')  # path to ChromeDriver.
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.implicitly_wait(30)  # Waits for elements to be ready before interacting with them.
    return driver
