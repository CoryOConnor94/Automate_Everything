from flask import Flask
from bs4 import BeautifulSoup
import requests
import jsonify


def get_currency_rate(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency_rate = soup.find('span', class_='ccOutputRslt').get_text()
    # print(f'1 {in_currency} is currently worth {currency_rate}')
    return currency_rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/eur-usd</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency_rate(in_cur, out_cur)
    result_dictionary = {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
    print(jsonify(result_dictionary))

app.run()


