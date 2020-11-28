# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import*
import sys
from qtUi.ToolsBarAndMenu import ToolsBarAndMenu
from PyQt5 import QtCore


app = QApplication(sys.argv)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
toolsEditot = ToolsBarAndMenu()
sys.exit(app.exec())

