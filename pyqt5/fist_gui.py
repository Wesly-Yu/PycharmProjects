# from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
app.setStyle('Fusion')
palette=QPalette()
palette.setColor(QPalette.ButtonText,Qt.red)
app.setPalette(palette)
window = QWidget()
window.resize(200,200)
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()