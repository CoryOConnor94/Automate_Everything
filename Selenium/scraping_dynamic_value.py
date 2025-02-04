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
    driver.get("http://automated.pythonanywhere.com")

    return driver


def clean_text(text):
    """
    Extracts and converts the temperature value from a given text string.

    Args:
        text (str): The input string containing a label and a numeric value (e.g., "Temperature: 23.5").

    Returns:
        float: The extracted numeric value as a float.
    """

    output = float(text.split(": ")[1])  # Split by ": " and convert the second part to float
    return output


def main():
    """
    Initializes the WebDriver, extracts temperature data from a webpage,
    processes it, and prints the result.
    """
    driver = get_driver()   # Initialize webdriver instance
    time.sleep(2)  # Allow time for the page to load

    try:
        # Locate the temperature element using XPath
        element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")

        # Extract and clean the temperature text
        temperature = clean_text(element.text)

        # Print the extracted temperature
        print(f'Average world temperature now is: {temperature}')
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()  # Ensure the browser closes properly


if __name__ == "__main__":
    main()
