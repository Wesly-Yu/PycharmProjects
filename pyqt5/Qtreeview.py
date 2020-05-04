import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets,QtGui,QtCore

class QtTreeWidget(QMainWindow):
    def __init__(self,parent=None):
        super(QtTreeWidget, self).__init__(parent)
        self.setWindowTitle(u"树控件")
        self.resize(800,600)
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        root = QTreeWidgetItem(self.tree)
        self.setCentralWidget(self.tree)
        root.setText(0, u'项目文件')
        root.setIcon(0, QIcon('./image/Open.png'))
        self.tree.setColumnWidth(0, 150)
        child1 = QTreeWidgetItem(root)
        child1.setText(0, u'子节点1')
        child1.setIcon(0, QIcon('./image/New.png'))
        child1.setCheckState(0, Qt.Checked)
        child1.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        child2 = QTreeWidgetItem(root)
        child2.setText(0, u'子节点2')
        child2.setIcon(0, QIcon('./image/New.png'))
        child2.setCheckState(0, Qt.Checked)
        child3 = QTreeWidgetItem(root)
        child3.setText(0, u'子节点3')
        child3.setIcon(0, QIcon('./image/New.png'))
        child3.setCheckState(0, Qt.Checked)
        self.tree.addTopLevelItem(root)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.rightClickMenu)

    # def onTreeClicked(self,pos):
    #     # screenPos = self.tree.mapToGlobal(pos)
    #     item = self.tree.currentItem()
    #     if item.parent() == None:
    #         print("key=%,value=%s" %(item.text(0),item.text(1)))

    def rightClickMenu(self,pos):
        try:
            item = self.tree.currentItem()
            self.contextMenu = QMenu()
            if item.parent() == None:
                self.actionA = self.contextMenu.addAction(u'增加')
                self.actionA.triggered.connect(self.actionAddHandler)
                self.contextMenu.exec_(self.mapToGlobal(pos))
                self.contextMenu.show()
            else:
                self.actionB = self.contextMenu.addAction(u'删除')
                self.actionC = self.contextMenu.addAction(u'重命名')
                self.actionB.triggered.connect(self.actionMoveHandler)
                self.actionC.triggered.connect(self.actionRenameHandler)
                self.contextMenu.exec_(self.mapToGlobal(pos))
                self.contextMenu.show()

        except Exception as e:
            print(e)
    def actionAddHandler(self):
        print(self.tree.currentItem().text(0))
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0,u'新增')
        node.setText(1,'new')
        # if item.parent() == None:
            # for i in range(0,item.childCount()):
            #     item.re
    def actionMoveHandler(self):
        print(self.tree.currentItem().text(0))
        item = self.tree.currentItem()
        for i in range(0, item.childCount()):
            print(item.child(item.childCount() - 1).text(0))
            item.removeChild(item.child(item.childCount() - 1))
    def actionRenameHandler(self):
        print(self.tree.currentItem().text(0))

    # def generateMenu(self,pos):
    #     print(pos)
    #     for i in self.tree.selectionModel().selection().index():
    #         rowNum = i.row
    #     if rowNum <2:
    #         menu = QMenu()
    #         item1 = menu.addAction("新增")
    #         item2 = menu.addAction("删除")
    #         item3 = menu.addAction("修改")
    #         screenPos = self.tree.mapToGlobal(pos)
    #         action = menu.exec(screenPos)
    #         if action == item1:
    #             print('选择了第一个')
    #         elif action == item2:
    #             print('选择了第二个')
    #         else:
    #             print("选择了第三个")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtTreeWidget()
    main.show()
    sys.exit(app.exec_())