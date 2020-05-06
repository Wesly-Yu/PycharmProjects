# ****
# 菜单栏(QMenu)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtGui

class CheckableDirModel(QFileSystemModel):
    def __init__(self, parent=None):
        QFileSystemModel.__init__(self, None)
        self.checks = {}

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.CheckStateRole:
            return QFileSystemModel.data(self, index, role)
        else:
            if index.column() == 0:
                return self.checkState(index)

    def flags(self, index):
        return QFileSystemModel.flags(self, index) | QtCore.Qt.ItemIsUserCheckable

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return QtCore.Qt.Checked

    def setData(self, index, value, role):
        if (role == QtCore.Qt.CheckStateRole and index.column() == 0):
            self.checks[index] = value
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
            return True
        return QFileSystemModel.setData(self, index, value, role)





class TreeViewDemo(QTreeView):
    def __init__(self, parent=None):
        super(TreeViewDemo, self).__init__(parent)

        # window系统提供的模式
        path = 'D://logs'
        self.model = CheckableDirModel()
        self.model.setRootPath(path)
        # self.model.setFilter()
        # 为控件添加模式。

        self.setModel(self.model)
        self.setRootIndex(self.model.index(path))  # 只显示设置的那个文件路径。
        self.setHeaderHidden(False)
        self.setColumnWidth(20,20)
        self.clicked.connect(self.file_name)  # 双击文件打开
        self.setWindowTitle("QTreeView例子")
        self.setColumnHidden(2,True)
        self.setColumnHidden(1, True)
        self.setColumnHidden(3,True)
        self.setObjectName('treeview')
        self.resize(640, 480)

    def file_name(self, Qmodelidx):
        print(self.model.filePath(Qmodelidx))  # 输出文件的地址。
        print(self.model.fileName(Qmodelidx))  # 输出文件名


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeViewDemo()
    tree.show()
    sys.exit(app.exec_())







