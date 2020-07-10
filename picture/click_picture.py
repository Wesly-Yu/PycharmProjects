#coding='utf-8'

import sys
import os
import qdarkstyle
from PyQt5 import QtGui, QtCore,QtWidgets


class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain
        # index = self.selectedIndexes()
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        s = QtCore.QSize(250, 200)
        if index.isValid() and role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(QtGui.QPixmap(self.listdata[index.row()]))
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(os.path.splitext(os.path.split(self.listdata[index.row()])[-1])[0])
        else:
            return QtCore.QVariant()

class MyListView(QtWidgets.QListView):
    """docstring for MyListView"""
    def __init__(self):
        super(MyListView, self).__init__()
        # show in Icon Mode
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setIconSize(QtCore.QSize(90, 90))
        self.setGridSize(QtCore.QSize(100, 100))
        crntDir = "D:/log"
        # create table
        list_data = []
        philes = os.listdir(crntDir)
        for phile in philes:
            if phile.endswith(".png"):
                list_data.append(os.path.join(crntDir, phile))
        lm = MyListModel(list_data, self)
        self.setModel(lm)
        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window =  MyListView()
    # window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
    window.setWindowOpacity(0.9)
    window.show()
    window.raise_()
    sys.exit(app.exec_())
