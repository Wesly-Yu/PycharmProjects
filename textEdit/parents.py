from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtCore
import sys
import os
import qdarkstyle
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

# class MyListModel(QtCore.QAbstractListModel):
#     def __init__(self, datain, parent=None, *args):
#         """ datain: a list where each item is a row
#         """
#         QtCore.QAbstractListModel.__init__(self, parent, *args)
#         self.listdata = datain
#     def rowCount(self, parent=QtCore.QModelIndex()):
#         return len(self.listdata)
#
#     def data(self, index, role):
#         s = QtCore.QSize(250, 200)
#         if index.isValid() and role == QtCore.Qt.DecorationRole:
#             return QtGui.QIcon(QtGui.QPixmap(self.listdata[index.row()]))
#         if index.isValid() and role == QtCore.Qt.DisplayRole:
#             # print(QtCore.QVariant(self.ListItemData[index.row()]['name']))
#             return QtCore.QVariant(os.path.splitext(os.path.split(self.listdata[index.row()])[-1])[0])
#         else:
#             return QtCore.QVariant()
#
#     def getItem(self, index):
#         if index > -1 and index < len(self.ListItemData):
#             return self.ListItemData[index]
#
# class MyListView(QtWidgets.QListView):
#     global image_list
#     """docstring for MyListView"""
#     def __init__(self,parent=None):
#         super(MyListView, self).__init__(parent)
#         self.Listview = QListView()
#         self.setViewMode(QtWidgets.QListView.IconMode)
#         self.setIconSize(QtCore.QSize(90, 90))
#         self.setGridSize(QtCore.QSize(110, 110))
#
#         crntDir = "D:\\log"
#         list_data = []
#         image_list = []
#         philes = os.listdir(crntDir)
#         for phile in philes:
#             if phile.endswith(".png"):
#                 list_data.append(os.path.join(crntDir, phile))
#                 image_list.append(phile)
#         self.List_data = list_data
#         print(self.List_data)
#         print(image_list)
#         lm = MyListModel(list_data)
#         self.setModel(lm)
#         self.show()
#         self.clicked.connect(self.onclicked)
#
#     def onclicked(self,item):
#         image_selected_path = self.List_data[item.row()]
#         print(image_selected_path)
#         self.close()
# class CompleterImage(QCompleter):
#     insertText = QtCore.pyqtSignal(str)
#     def __init__(self, parent=None):
#         #toolIcon name in image_list
#         crntDir = "D:\\log"
#         image_list = []
#         philes = os.listdir(crntDir)
#         for phile in philes:
#             if phile.endswith(".png"):
#                 image_list.append(phile)
#         # print(image_list)
#         QCompleter.__init__(self,image_list, parent)
#         self.setCompletionMode(QCompleter.PopupCompletion)
#         self.highlighted.connect(self.setHighlighted)
#     def setHighlighted(self, text):
#         self.lastSelected = text
#
#     def getSelected(self):
#         return self.lastSelected

class CompleterWords(QCompleter):
    insertText = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        insertText = QtCore.pyqtSignal(str)
        crntDir = "D:\\log"
        image_list = []
        philes = os.listdir(crntDir)
        for phile in philes:
            if phile.endswith(".png"):
                image_list.append(phile)
        print(image_list)
        keywords_list = ['open browser', 'click', 'input text', 'contain', 'log', 'clear',
                         'clearcookies', 'doubleclick', 'scrol to view', 'should', 'reload',
                         'and', 'wait', 'children', 'right click', '.rightclick()', 'read file'
            , 'equal']
        #toolIcon name in image_list
        QCompleter.__init__(self,image_list, parent)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.highlighted.connect(self.setHighlighted)
    def setHighlighted(self, text):
        self.lastSelected = text

    def getSelected(self):
        return self.lastSelected

