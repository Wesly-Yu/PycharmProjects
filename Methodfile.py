
from  NewMainWindows import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import os





def getFilsName(self, path):
    filenamedict = []
    root=None
    for root, dirs, files in os.walk(path):
        for file in files:
            filenamedict.append(file)
    return filenamedict,root




