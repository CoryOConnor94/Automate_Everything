from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time


service = Service('chromedriver-win64/chromedriver.exe')


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")

    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = (text.split(": ")[1])
    return output


def get_date_time():
    date_time = datetime.now()
    formatted_datetime = date_time.strftime('%y-%m-%d-%H-%M-%S')
    return formatted_datetime


def save_to_file(formatted_datetime, current_temp):
    with open(formatted_datetime, "w") as file:
        file.write(current_temp)


def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")
        temperature = clean_text(element.text)
        formatted_datetime = get_date_time()
        save_to_file(formatted_datetime, temperature)


if __name__ == "__main__":
    main()
