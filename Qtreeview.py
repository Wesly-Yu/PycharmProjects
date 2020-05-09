from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import  QSortFilterProxyModel
from PyQt5.QtWidgets import QFileSystemModel



class FileTreeSelectorModel(QtWidgets.QFileSystemModel):
    def __init__(self, parent=None, rootpath='/'):
        QtWidgets.QFileSystemModel.__init__(self, None)
        self.root_path      = rootpath
        self.checks         = {}
        self.nodestack      = []
        self.parent_index   = self.setRootPath(self.root_path)
        self.root_index     = self.index(self.root_path)

        # self.setFilter(QtCore.QDir.AllEntries | QtCore.QDir.Hidden | QtCore.QDir.NoDot)
        self.directoryLoaded.connect(self._loaded)

    def _loaded(self, path):
        print('loaded', self.root_path, self.rowCount(self.parent_index))

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.CheckStateRole:
            return QtWidgets.QFileSystemModel.data(self, index, role)
        else:
            if index.column() == 0:
                return self.checkState(index)

    def flags(self, index):
        return QtWidgets.QFileSystemModel.flags(self, index) | QtCore.Qt.ItemIsUserCheckable

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return QtCore.Qt.Checked

    def setData(self, index, value, role):
        if (role == QtCore.Qt.CheckStateRole and index.column() == 0):
            self.checks[index] = value
            print('setData(): {}'.format(value))
            return True
        return QtWidgets.QFileSystemModel.setData(self, index, value, role)

    def traverseDirectory(self, parentindex, callback=None):
        print('traverseDirectory():')
        callback(parentindex)
        if self.hasChildren(parentindex):
            print('|children|: {}'.format(self.rowCount(parentindex)))
            for childRow in range(self.rowCount(parentindex)):
                childIndex = parentindex.child(childRow, 0)
                print('child[{}]: recursing'.format(childRow))
                self.traverseDirectory(childIndex, callback=callback)
        else:
            print('no children')

    def printIndex(self, index):
        print('model printIndex(): {}'.format(self.filePath(index)))


class ProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._root_path = ""

    def filterAcceptsRow(self, source_row, source_parent):
        source_model = self.sourceModel()
        if self._root_path and isinstance(source_model, QFileSystemModel):
            root_index = source_model.index(self._root_path).parent()
            if root_index == source_parent:
                index = source_model.index(source_row, 0, source_parent)
                return index.data(QFileSystemModel.FilePathRole) == self._root_path
        return True

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, p):
        self._root_path = p
        self.invalidateFilter()


# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.create_treeview()
#         self.setCentralWidget(self.treeView)
#
#     def create_treeview(self):
#
#         self.root_path = "D:/logs"
#
#         self.treeView = QTreeView()
#         self.treeView.setObjectName("treeView")
#
#         self.dirModel = FileTreeSelectorModel(rootpath=self.root_path)
#         self.dirModel.setRootPath(QDir.rootPath())
#         root_index = self.dirModel.index(self.root_path).parent()
#
#         self.proxy = ProxyModel(self.dirModel)
#         self.proxy.setSourceModel(self.dirModel)
#         self.proxy.root_path = self.root_path
#
#         self.treeView.setModel(self.proxy)
#
#         proxy_root_index = self.proxy.mapFromSource(root_index)
#         self.treeView.setRootIndex(proxy_root_index)
#         self.treeView.setColumnHidden(1, True)
#         self.treeView.setColumnHidden(2, True)
#         self.treeView.setColumnHidden(3, True)
#         self.treeView.setHeaderHidden(True)
#         self.treeView.clicked.connect(self.tree_click)
#
#     @pyqtSlot(QModelIndex)
#     def tree_click(self, index):
#         ix = self.proxy.mapToSource(index)
#         print(
#             ix.data(QFileSystemModel.FilePathRole),
#             ix.data(QFileSystemModel.FileNameRole),
#         )


# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec_())