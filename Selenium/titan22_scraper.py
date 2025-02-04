from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

# Retrieve credentials from environment variables.
USERNAME = os.environ['']
PASSWORD = os.environ['']

# Define the path to the ChromeDriver executable
service = Service('chromedriver.exe')


def get_driver():
    """
    Initializes and configures a Selenium WebDriver instance for Chrome.

    Returns:
        WebDriver: An instance of Chrome WebDriver with predefined options.
    """

    # Set Chrome options to enhance stability and avoid detection
    options = webdriver.ChromeOptions()

    # Disable the "Chrome is being controlled by automated test software" infobar
    options.add_argument("disable-infobars")

    # Start the browser in a maximized window
    options.add_argument("start-maximized")

    # Prevent Chrome from using shared memory, useful in Docker or CI/CD environments
    options.add_argument("disable-dev-shm-usage")

    # Disable the Chrome sandbox for environments where it may cause issues
    options.add_argument("no-sandbox")

    # Prevent Selenium from being detected by excluding automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Further obfuscate automation detection by disabling Blink automation flags
    options.add_argument("disable-blink-features=AutomationControlled")

    # Create a WebDriver instance with the specified options
    driver = webdriver.Chrome(service=service, options=options)

    # Open the target webpage
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")

    return driver


def login(driver):
    """
    Logs into the website by entering the username and password,
    then navigates to the homepage.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
    """

    # Locate the username field and enter the stored username
    driver.find_element(by="xpath", value='//*[@id="CustomerEmail"]').send_keys(USERNAME)

    # Pause briefly to simulate real user behavior (optional but helps avoid detection)
    time.sleep(2)

    # Locate the password field and enter the stored passwor
    driver.find_element(by="xpath", value='//*[@id="CustomerPassword"]').send_keys(PASSWORD)

    # Click the login button to submit the form
    driver.find_element(by="xpath", value='//*[@id="customer_login"]/button').click()

    # Click on a navigation link after login
    driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()

    # Print the current URL to verify successful login
    print(driver.current_url)


def main():
    """
     Initializes the WebDriver and performs the login process.
     """
    driver = get_driver()
    login(driver)


if __name__ == "__main__":
    main()
