import sys
from PyQt5 import QtWidgets, QtCore
from Qtreeview import ProxyModel

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
        print('_loaded', self.root_path, self.rowCount(self.parent_index))

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





class FileTreeSelectorDialog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.root_path = 'D:/logs'

        # Widget
        self.title= "Application Window"
        self.left= 200
        self.top= 200
        self.width= 400
        self.height= 400

        self.setWindowTitle(self.title)         #TODO:  Whilch title?
        self.setGeometry(self.left, self.top, self.width, self.height)
        # filter1 = ['*.txt']
        # Model
        self.model= FileTreeSelectorModel(rootpath=self.root_path)
        # self.model          = QtWidgets.QFileSystemModel()
        # self.model.setNameFilters(filter1)
        self.model.setNameFilterDisables(0)
        # View
        self.view= QtWidgets.QTreeView()

        self.view.setObjectName('treeView_fileTreeSelector')
        self.view.setWindowTitle("Dir View")    #TODO:  Which title?
        self.view.resize(300, 200)

        # Attach Model to View
        self.view.setModel(self.model)
        index = self.model.index(self.root_path)
        self.view.setRootIndex(self.model.index(self.root_path))
        self.view.setColumnWidth(0, 50)
        self.view.setColumnHidden(1, True)
        self.view.setColumnHidden(2, True)
        self.view.setColumnHidden(3, True)
        self.proxy = ProxyModel(self.model)
        self.proxy.setSourceModel(self.model)
        self.proxy.root_path = self.root_path
        self.view.setModel(self.proxy)
        proxy_root_index = self.proxy.mapFromSource(index)
        self.view.setRootIndex(proxy_root_index)
        # Misc
        self.node_stack= []

        # GUI
        windowlayout = QtWidgets.QVBoxLayout()
        windowlayout.addWidget(self.view)
        self.setLayout(windowlayout)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_fileTreeSelector_clicked(self, index):
        print('tree clicked: {}'.format(self.model.filePath(index)))
        self.model.traverseDirectory(index, callback=self.model.printIndex)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = FileTreeSelectorDialog()
    sys.exit(app.exec_())