from bs4 import BeautifulSoup
import requests


def get_currency_rate(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency_rate = soup.find('span', class_='ccOutputRslt').get_text()
    print(f'1 {in_currency} is currently worth {currency_rate}')


def main():
    get_currency_rate('EUR', 'USD')


if __name__ == "__main__":
    main()

