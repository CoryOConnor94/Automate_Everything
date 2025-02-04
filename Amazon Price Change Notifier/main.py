from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from twilio.rest import Client
from datetime import datetime as dt
import time

service = Service('../chromedriver-win64/chromedriver.exe')


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
    driver.get("")

    return driver


def get_price(driver):
    element = driver.find_element(by='', value='')
    return element.text


def clean_price(price):
    return float(price.replace('$', ''))


def main():
    account_sid = ''
    account_token = ''
    client = Client(account_sid, account_token)
    driver = get_driver()
    prices = []
    while True:
        time.sleep(10)
        current_price = get_price(driver)
        cleaned_price = clean_price(current_price)
        prices.append(cleaned_price)
        if prices[-1] < prices[-2]:
            message = client.messages.create(
                body=f'Price has now dropped to ${cleaned_price}'
                     f'Hurry up and buy!',
                from_='',
                to=''
            )
        del prices[-2]


if __name__ == "__main__":
    main()
