from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests


def get_currency_rate(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency_rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(currency_rate[:-4])

    return rate


def convert_currency():
    input_amount = float(text.text())
    in_cur = in_combo.currentText()
    out_cur = out_combo.currentText()
    print(in_cur, out_cur)
    rate = get_currency_rate(in_cur, out_cur)
    converted_currency = round(input_amount * rate, 2)
    message = f'{input_amount} {in_cur} Converts to {converted_currency} {out_cur}'
    output_label.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

layout_one = QHBoxLayout()
layout.addLayout(layout_one)

output_label = QLabel('')
layout.addWidget(output_label)

layout_two = QVBoxLayout()
layout_one.addLayout(layout_two)

layout_three = QVBoxLayout()
layout_one.addLayout(layout_three)


in_combo = QComboBox()
currencies = ['EUR', 'USD', 'GBP']
in_combo.addItems(currencies)
layout_two.addWidget(in_combo)

out_combo = QComboBox()
out_combo.addItems(currencies)
layout_two.addWidget(out_combo)


text = QLineEdit()
layout_three.addWidget(text)

btn = QPushButton('Convert Currency')
layout_three.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(convert_currency)

window.setLayout(layout)
window.show()
app.exec()
