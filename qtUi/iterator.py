#coding='utf-8'
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import  QSortFilterProxyModel
from PyQt5.QtWidgets import QFileSystemModel




class FileTreeSelectorModel(QtWidgets.QFileSystemModel):
    def __init__(self, parent=None, rootpath='/'):
        QtWidgets.QFileSystemModel.__init__(self, None)
        # self.setFilter(QtCore.QDir.AllEntries | QtCore.QDir.Hidden | QtCore.QDir.NoDot)

    # def treeview(self):

