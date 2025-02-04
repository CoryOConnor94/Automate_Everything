from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

USERNAME = 'automated'
PASSWORD = 'automatedautomated'

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
    driver.get("http://automated.pythonanywhere.com/login/")

    return driver


def login(driver):
    driver.find_element(by='id', value="id_username").send_keys(USERNAME)
    time.sleep(2)
    driver.find_element(by='id', value="id_password").send_keys(PASSWORD)
    driver.find_element(by='xpath', value='/html/body/div[1]/div/div/div[3]/form/button').click()
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    print(driver.current_url)


def main():
    driver = get_driver()
    login(driver)


if __name__ == "__main__":
    main()
