# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  NewMainWindows import Ui_MainWindow
from  ToolsBarAndMenu import ToolsBarAndMenu



app = QApplication(sys.argv)
toolsEditot = ToolsBarAndMenu()
sys.exit(app.exec())

