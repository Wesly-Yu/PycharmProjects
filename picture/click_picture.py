#coding='utf-8'

import sys
import os
import qdarkstyle
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        s = QtCore.QSize(250, 200)
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

class MyListView(QtWidgets.QListView):
    """docstring for MyListView"""
    def __init__(self,parent=None):
        super(MyListView, self).__init__(parent)
        self.Listview = QListView()
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setIconSize(QtCore.QSize(90, 90))
        self.setGridSize(QtCore.QSize(110, 110))

        crntDir = "D:\\log"
        list_data = []
        philes = os.listdir(crntDir)
        for phile in philes:
            if phile.endswith(".png"):
                list_data.append(os.path.join(crntDir, phile))
        self.List_data = list_data

        print(self.List_data)
        lm = MyListModel(list_data)
        self.setModel(lm)
        self.show()
        self.clicked.connect(self.onclicked)

    def onclicked(self,item):
        image_selected_path = self.List_data[item.row()]
        print(image_selected_path)
        self.close()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyListView()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
    window.setWindowOpacity(0.9)
    window.show()
    window.raise_()
    sys.exit(app.exec_())
