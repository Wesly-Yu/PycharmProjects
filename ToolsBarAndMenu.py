from  NewMainWindows import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import os
from Methodfile import getFilsName
import  xlwt

class ToolsBarAndMenu(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(ToolsBarAndMenu,self).__init__(parent)
        self.setupUi(self)
        self.iniUI()
        self.initFixtureSourece()
        self.actionNewFile.triggered.connect(self.FileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExite.triggered.connect(self.ExitTool)
        self.tree.customContextMenuRequested.connect(self.rightClickMenu1)
        self.tree.clicked.connect(self.leftClickScrolToCentrol)
        self.tree2.customContextMenuRequested.connect(self.rightClickMenu2)
        self.show()
        cypressDefaultPath = 'C:\\Users\\Administrator\\cypress\\integration'


    def iniUI(self):
        self.tree = self.treeWidget1
        self.tree2 = self.treeWidget_2
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.updateEditorData()
        self.tree.updatesEnabled()
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dialog = QtWidgets.QDialog()
        self.flo = QFormLayout()




    def leftClickScrolToCentrol(self):
        item = self.tree.currentItem()
        self.tree.setCurrentItem(item)
        self.tree.scrollToItem(item, QAbstractItemView.PositionAtCenter)







    def ExitTool(self):
        self.close()


    def FileNew(self):
        global dialog
        global pNormalLineEdit
        global pPasswordLineEdit
        self.dialog.resize(400,150)
        self.dialog.setWindowTitle('设置文件名以及路径')
        btn1= QPushButton('确定',self.dialog)
        btn1.move(80,90)
        btn2 = QPushButton('退出',self.dialog)
        btn2.move(200,90)
        pNormalLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        self.flo.addRow(u"文件夹名称", pNormalLineEdit)
        self.flo.addRow(u"文件夹路径", pPasswordLineEdit)
        pNormalLineEdit.setMaxLength(8)
        pPasswordLineEdit.setPlaceholderText("C:\\Users\\Administrator\\cypress\\integration")
        self.dialog.setLayout(self.flo)
        btn1.clicked.connect(self.text_ok)
        btn2.clicked.connect(self.dialog.close)
        self.dialog.exec_()

    def text_ok(self):
        cypressProjectPath = r'C:\Users\Administrator\cypress\integration'
        DirNameCreate = pNormalLineEdit.text()
        if DirNameCreate:
            DirNameCreate =str(DirNameCreate)
            os.mkdir(cypressProjectPath + './' +DirNameCreate)
            self.dialog.exec_()
        else:
            QtWidgets.QMessageBox.about(self, "警告", "请重新输入英文文件夹名称(中文识别有误)")
        QtWidgets.QMessageBox.about(self,"说明","创建文件夹成功") #弹窗
        self.dialog.close()






    def openFile(self):
        self.tree.headerItem().setText(0, "工程目录")
        self.tree.setColumnCount(1)
        self.tree.updateEditorData()
        self.tree.expandAll()
        Dirpath = QFileDialog.getExistingDirectory(self,'Open File','./home')
        DirName = str(Dirpath).split('/')[-1]
        root = QTreeWidgetItem(self.tree)
        root.setIcon(0, QIcon('./image/Open.png'))
        root.setText(0,DirName)
        root.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        filenames = getFilsName(self, Dirpath)

        if len(filenames) !=0:
                for filename in filenames:
                    child = QTreeWidgetItem(root)
                    child.setText(0,filename)
                    child.setIcon(0, QIcon('./image/New.png'))
                    child.setCheckState(0, Qt.Unchecked)
        else:
            QMessageBox.about(self,'消息','当前文件夹下为空')

    def initFixtureSourece(self):
        sourcePath='C:\\Users\\Administrator\\cypress\\fixtures'
        self.tree2.setColumnCount(1)
        self.tree2.expandAll()
        soureceRoot = QTreeWidgetItem(self.tree2)
        soureceName = str(sourcePath).split('\\')[-1]
        soureceRoot.setIcon(0, QIcon('./image/Open.png'))
        soureceRoot.setText(0, soureceName)
        filenames = getFilsName(self, sourcePath)
        for filename in filenames:
            child = QTreeWidgetItem(soureceRoot)
            child.setText(0, filename)
            child.setIcon(0, QIcon('./image/New.png'))
            child.setCheckState(0, Qt.Unchecked)
            # child.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
    #编辑用例 树框中的数据
    def rightClickMenu1(self,position1):
        try:
            item = self.tree.currentItem()
            self.contextMenu = QMenu(self.tree)
            if item.parent() == None:
                self.actionA = self.contextMenu.addAction(u'新增用例')
                self.actionC = self.contextMenu.addAction(u'重命名文件夹')
                self.actionA.triggered.connect(self.actionAddFileHandler)
                self.actionC.triggered.connect(self.actionRenameDirHandler)
                self.contextMenu.exec_(self.tree.mapToGlobal(position1))
                self.contextMenu.show()
            else:
                self.actionE = self.contextMenu.addAction(u'重命名文件')
                self.actionB = self.contextMenu.addAction(u'删除选中的文件')
                self.actionB.triggered.connect(self.actionMoveHandler)
                self.actionE.triggered.connect(self.actionRenameFileHandler)
                self.contextMenu.exec_(self.tree.mapToGlobal(position1))
                self.contextMenu.show()


        except Exception as e:
            print(e)
    # 编辑po公共参数 树框中的数据
    def rightClickMenu2(self,position2):
        try:
            item2 = self.tree2.currentItem()
            self.contextMenu = QMenu(self.tree)
            if item2.parent() == None:
                self.actionE = self.contextMenu.addAction(u'增加')
                self.actionE.triggered.connect(self.actionAddHandler)
                self.contextMenu.exec_(self.tree2.mapToGlobal(position2))
                self.contextMenu.show()
            else:
                self.actionF = self.contextMenu.addAction(u'删除')
                self.actionF.triggered.connect(self.actionMoveHandler)
                self.contextMenu.exec_(self.tree2.mapToGlobal(position2))
                self.contextMenu.show()


        except Exception as e:
            print(e)

    #向用例树中添加测试文件
    def actionAddFileHandler(self):
        print(self.tree.currentItem().text(0))
        item = self.tree.currentItem()
        # renameDirPath =cypressDefaultPath+"\\"+'item'
        # node = QTreeWidgetItem(item)
        # node.setText(0,'new.xlsx')
        # node.setIcon(0, QIcon('./image/New.png'))
        # node.setCheckState(0, Qt.Unchecked)
        # workbook = xlwt.Workbook(encoding='utf-8')
        # sheet1 = workbook.add_sheet('sheet1')
        # workbook.save(renameDirPath+'\\'+"new.xlsx")

    #重命名用例树文件夹选定的文件
    def actionRenameDirHandler(self):
        print(self.tree.currentItem().text(0))
        item2 = self.tree2.currentItem()
        node = QTreeWidgetItem(item2)
        node.setText(1, 'new')
    #删除用例树中不需要的用例
    def actionMoveHandler(self):
        print(self.tree.currentItem().text(0))
        item = self.tree.currentItem()
        for i in range(0, item.childCount()):
            print(item.child(item.childCount() - 1).text(0))
            item.removeChild(item.child(item.childCount() - 1))
    #删除公共参数 框中的文件
    def actionMoveHandler2(self):
        print(self.tree2.currentItem().text(0))
        item2 = self.tree2.currentItem()
        for i in range(0, item2.childCount()):
            print(item2.child(item2.childCount() - 1).text(0))
            item2.removeChild(item2.child(item2.childCount() - 1))

    #重命名用例树中选定的文件
    def actionRenameFileHandler(self):
        pass



