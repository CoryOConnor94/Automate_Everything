from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

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
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")

    return driver


def check_stock_price(driver):
    """
    Retrieves the stock price change percentage from the website.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.

    Returns:
        float: The percentage change in stock price.
    """

    # Wait for the page to load to ensure elements are available
    time.sleep(2)

    # Click the "Reject Cookies" button to proceed (if present)
    reject_cookies = driver.find_element(by='xpath', value='//*[@id="CybotCookiebotDialogBodyButtonDecline"]').click()

    # Wait for the page to update after rejecting cookies
    time.sleep(5)

    # Locate the element containing the stock price change percentage
    current_price_change = driver.find_element(by='xpath',
                                               value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')

    # Extract the percentage, remove the '%' symbol, and convert it to a float
    price_change_percent = float(current_price_change.text.replace('%', '').strip())

    return price_change_percent


def main():
    """
    Initializes the WebDriver and checks for significant stock price changes.
    """
    driver = get_driver()  # Initialize the Selenium WebDriver instance

    # Fetch the stock price change percentage
    price_change = check_stock_price(driver)

    # If the stock price change is greater than 0.1%, trigger an alert
    if price_change > 0.07:
        print(f"Alert: The stock price has changed by {price_change}%")

if __name__ == '__main__':
    main()
