from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")

    return driver


def check_stock_price(driver):
    time.sleep(2)
    reject_cookies = driver.find_element(by='xpath', value='//*[@id="CybotCookiebotDialogBodyButtonDecline"]').click()
    time.sleep(5)
    current_price_change = driver.find_element(by='xpath', value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    price_change_percent = float(current_price_change.text.replace('%', '').strip())
    return price_change_percent

def main():
    driver = get_driver()
    price_change = check_stock_price(driver)
    if price_change > 0.1:
        print(f"Alert the stock price has changed by {price_change}%")


if __name__ == '__main__':
    main()
