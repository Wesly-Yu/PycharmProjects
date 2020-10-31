import sys
from PyQt5 import QtGui, QtCore,QtWidgets
import csv
import xlrd

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.initUI()

    def initUI(self):

        global itemText
        global descText

        item = QtWidgets.QLabel('Item')
        itemEdit = QtWidgets.QLineEdit()
        itemText = str(itemEdit)
        desc = QtWidgets.QLabel('Description (optional)')
        descEdit = QtWidgets.QTextEdit()
        descText = str(descEdit)
        add = QtWidgets.QPushButton("Add item")

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(item, 1, 0)
        grid.addWidget(itemEdit, 1, 1)

        grid.addWidget(desc, 2, 0)
        grid.addWidget(descEdit, 2, 1, 3, 1)

        grid.addWidget(add, 6, 1)

        add.clicked.connect(self.writeFile)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Add to list")
        self.show()

    def writeFile(self):
        tabeles= xlrd.open_workbook('D:log/new1.xls')
        csvwriter = csv.writer(tabeles)
        csvwriter.writerow([itemText, descText])
        print(itemText)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()