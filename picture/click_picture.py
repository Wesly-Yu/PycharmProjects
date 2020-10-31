#coding='utf-8'
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit,QHBoxLayout,QWidget
import sys
import os
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor,QTextLine


#-----------主弹窗-----------------------#

class MyMainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(MyMainWindow, self).__init__()

        layout = QHBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)
        self.line = QTextLine()
        self.textedit = QPlainTextEdit()
        self.textedit.textChanged.connect(self.save_text)
        layout.addWidget(self.textedit)


    def save_text(self):
        list = ["baidu","test","screenshotaaa","search"]
        text = self.textedit.toPlainText()
        lines_last_words = text.split("\n")[-1].split(" ")[-1]
        self.picwindow = ImgListView(lines_last_words)
        self.picwindow.resize(130,130)
        self.picwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        if lines_last_words in list:
            self.picwindow.show()
            popup_pos = self.textedit.cursorRect()
            x = popup_pos.x()
            y = popup_pos.height()
            pos2 = self.mapToGlobal(QPoint(1.2*x,2*y))
            self.picwindow.move(pos2)
            self.picwindow.setStyleSheet("border :1px solid black;")
            self.picwindow.raise_()

        else:
            self.picwindow.hide()
        with open('mytextfile.txt', 'w') as f:
            f.write(text)

#----------小弹窗----------#

class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        if index.isValid() and role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(QtGui.QPixmap(self.listdata[index.row()]))
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            # print(QtCore.QVariant(self.ListItemData[index.row()]['name']))
            return QtCore.QVariant(os.path.splitext(os.path.split(self.listdata[index.row()])[-1])[0])
        else:
            return QtCore.QVariant()

    def getItem(self, index):
        if index > -1 and index < len(self.ListItemData):
            return self.ListItemData[index]



class ImgListView(QtWidgets.QListView):
    """docstring for MyListView"""
    def __init__(self,imagename,parent=None):
        super(ImgListView, self).__init__(parent)
        self.Listview = QListView()
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setIconSize(QtCore.QSize(110, 110))
        self.setGridSize(QtCore.QSize(120, 120))

        crntDir = "/Users/yupeng55/Documents/PycharmProjects/pyqt5/icon/"
        list_data = []
        target_file = crntDir+imagename+".jpg"
        list_data.append(target_file)
        self.List_data = list_data
        lm = MyListModel(list_data)
        self.setModel(lm)
        self.show()
        self.clicked.connect(self.onclicked)

    def onclicked(self,item):
        image_selected_path = self.List_data[item.row()]
        self.close()




def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    form = MyMainWindow()
    form.resize(800,800)
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

