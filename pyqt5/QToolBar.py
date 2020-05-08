# ****
# 工具栏(QMenu)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtWidgets


class FileSystemView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        super(FileSystemView, self).__init__(parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.homePath())
        self.setModel(self.model)
        self.setRootIndex(self.model.index(QtCore.QDir.homePath()))
        self.model.setReadOnly(False)
        self.setAnimated(False)
        self.setSortingEnabled(True)
        self.setEditTriggers(QtWidgets.QTreeView.NoEditTriggers)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)


    def showContextMenu(self, point):
        ix = self.indexAt(point)
        if ix.column() == 0:
            menu = QtWidgets.QMenu()
            menu.addAction("Rename")
            action = menu.exec_(self.mapToGlobal(point))
            if action:
                if action.text() == "Rename":
                    self.edit(ix)


if __name__ == '__main__':
    import sys

    app =QtWidgets.QApplication(sys.argv)
    w = FileSystemView()
    w.show()
    sys.exit(app.exec_())