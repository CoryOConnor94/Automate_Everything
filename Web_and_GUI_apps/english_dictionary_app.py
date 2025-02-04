from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
import json


dictionary_data = json.load(open('data.json'))


def get_definition():
    word = user_input.text()
    word = word.lower()
    if word in dictionary_data:
        results = dictionary_data[word]
        output_label.setText('\n'.join(results))
    else:
        output_label.setText('Word not found')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Dictionary')

layout = QVBoxLayout()

layout_one = QHBoxLayout()
layout.addLayout(layout_one)

layout_two = QHBoxLayout()
layout.addLayout(layout_two)

user_input = QLineEdit()
layout_one.addWidget(user_input)

btn = QPushButton('Get Definition')
layout_one.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(get_definition)

output_label = QLabel('')
output_label.setFixedSize(600, 50)
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
