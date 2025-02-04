from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
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
        str: The extracted temperature value.
    """

    output = text.split(": ")[1]  # Split by ": " and convert the second part to float
    return output


def get_date_time():
    """
    Gets the current date and time, then formats it as a string.

    Returns:
        str: The formatted date-time string in 'yy-mm-dd-HH-MM-SS' format.
    """
    date_time = datetime.now()  # Get the current date and time
    formatted_datetime = date_time.strftime('%y-%m-%d-%H-%M-%S')  # Format it as 'yy-mm-dd-HH-MM-SS'
    return formatted_datetime


def save_to_file(formatted_datetime, current_temp):
    """
    Saves the current temperature to a file named with the current date and time.

    Args:
        formatted_datetime (str): The formatted date-time string used as the filename.
        current_temp (str): The temperature value to save in the file.
    """
    with open(formatted_datetime, "w") as file:  # Open a file with the date-time as the name
        file.write(current_temp)  # Write the temperature data


def main():
    """
    Initializes the WebDriver and continuously extracts temperature data from a webpage.
    Saves each recorded temperature with a timestamped filename.
    """
    driver = get_driver()   # Initialize webdriver instance

    while True:
        time.sleep(2)  # Wait for 2 seconds before fetching data again

        # Locate the temperature element on the webpage
        element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")

        # Extract and clean the temperature text
        temperature = clean_text(element.text)

        # Get a timestamp for the file name
        formatted_datetime = get_date_time()

        # Save the temperature data to a timestamped file
        save_to_file(formatted_datetime, temperature)

if __name__ == "__main__":
    main()
