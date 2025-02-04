from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

USERNAME = 'mitchconnor886@gmail.com'
PASSWORD = 'automate'

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
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")

    return driver


def login(driver):
    driver.find_element(by="xpath", value='//*[@id="CustomerEmail"]').send_keys(USERNAME)
    driver.find_element(by="xpath", value='//*[@id="CustomerPassword"]').send_keys(PASSWORD)
    driver.find_element(by="xpath", value='//*[@id="customer_login"]/button').click()
    driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()

def main():
    driver = get_driver()
    login(driver)



if __name__ == "__main__":
    main()