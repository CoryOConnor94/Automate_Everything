from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Files destroyed')


app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. '
                     'The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setToolTip('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()
app.exec()
