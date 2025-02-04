from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    driver.get("http://automated.pythonanywhere.com")

    return driver


def main():
    """
    Main function to initialize WebDriver and extract text from a specific element.
    """
    driver = get_driver() # Initialize webdriver instance

    try:
        # Locate the target element using XPath
        element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[12]")

        # Print the extracted text
        print(element.text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the browser closes after execution
        driver.quit()


if __name__ == "__main__":
    main()
