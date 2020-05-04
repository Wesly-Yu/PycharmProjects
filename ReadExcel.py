import xlrd
from  NewMainWindows import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import os


def read_excel(QTableWidget):
    data = xlrd.open_workbook('./test1.xlsx')
    datas = data.sheet_names()
    worksheet1 = data.sheet_by_name(u'sheet1')
    table = data.sheet_by_index(0)
    cols = table.ncols  # 列
    rows = table.nrows  # 行
    talbles = []
    for row in range(rows):
        cell_content_row = worksheet1.row(row)
        for col in range(cols):
            if cell_content_row[col] is not '':
                talbles.append(cell_content_row[col])
            else:
                talbles.append(cell_content_row[col])

    print(talbles)
