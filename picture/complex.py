#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QGridLayout,QPushButton
import sys

class pop(QtWidgets.QWidget):
    def __init__(self,):
        super(pop, self).__init__()
        layout = QGridLayout(self)
        button = QPushButton("看这里啊啊")
        layout.addWidget(button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.adjustSize()
        self.setWindowFlags(Qt.Popup)
        point= self.rect().bottomRight()
        global_point = self.mapToGlobal(point)
        # self.move(global_point)
        self.move(global_point - QPoint(self.width(), 0))

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.button = QPushButton('Hit this button to show a popup', self)
        self.button.clicked.connect(self.handleOpenDialog)
        self.button.move(250, 80)
        self.resize(600, 200)

    def handleOpenDialog(self):
        self.popup = pop()
        self.popup.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())