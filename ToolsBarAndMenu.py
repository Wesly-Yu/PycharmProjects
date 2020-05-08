from  NewMainWindows import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Methodfile import createNewFile
import  xlwt
from iterator import createCounter
import os
from  Qtreeview import FileTreeSelectorModel,ProxyModel


class ToolsBarAndMenu(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(ToolsBarAndMenu,self).__init__(parent)
        self.setupUi(self)
        self.iniUI()
        self.initFixtureSourece()
        # self.actionNewFile.triggered.connect(self.FileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExite.triggered.connect(self.ExitTool)
        self.tree.customContextMenuRequested.connect(self.rightClickMenu1)
        # self.tree.clicked.connect(self.leftClickScrolToCentrol)
        # self.tree2.customContextMenuRequested.connect(self.rightClickMenu2)
        self.show()


    def iniUI(self):
        self.tree = self.treeview1
        self.tree2 = self.treeview2
        self.tree.setEditTriggers(self.tree.NoEditTriggers)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dialog = QtWidgets.QDialog()
        self.flo = QFormLayout()




    # def leftClickScrolToCentrol(self):
    #     item = self.tree.currentItem()
    #     self.tree.setCurrentItem(item)
    #     self.tree.scrollToItem(item, QAbstractItemView.PositionAtCenter)







    def ExitTool(self):
        self.close()


    # def FileNew(self):
    #     global dialog
    #     global pNormalLineEdit
    #     global pPasswordLineEdit
    #     self.dialog.resize(400,150)
    #     self.dialog.setWindowTitle('设置文件名以及路径')
    #     btn1= QPushButton('确定',self.dialog)
    #     btn1.move(80,90)
    #     btn2 = QPushButton('退出',self.dialog)
    #     btn2.move(200,90)
    #     pNormalLineEdit = QLineEdit()
    #     pPasswordLineEdit = QLineEdit()
    #     self.flo.addRow(u"文件夹名称", pNormalLineEdit)
    #     self.flo.addRow(u"文件夹路径", pPasswordLineEdit)
    #     pNormalLineEdit.setMaxLength(8)
    #     pPasswordLineEdit.setPlaceholderText("C:\\Users\\Administrator\\cypress\\integration")
    #     self.dialog.setLayout(self.flo)
    #     btn1.clicked.connect(self.text_ok)
    #     btn2.clicked.connect(self.dialog.close)
    #     self.dialog.exec_()
    #
    # def text_ok(self):
    #     cypressProjectPath = r'C:\Users\Administrator\cypress\integration'
    #     DirNameCreate = pNormalLineEdit.text()
    #     if DirNameCreate:
    #         DirNameCreate =str(DirNameCreate)
    #         os.mkdir(cypressProjectPath + './' +DirNameCreate)
    #         self.dialog.exec_()
    #     else:
    #         QtWidgets.QMessageBox.about(self, "警告", "请重新输入英文文件夹名称(中文识别有误)")
    #     QtWidgets.QMessageBox.about(self,"说明","创建文件夹成功") #弹窗
    #     self.dialog.close()
    #
    #
    #
    #
    #
    #
    def openFile(self):
        self.tree.expandAll()
        Dirpath = QFileDialog.getExistingDirectory(self,'Open File','./home')
        print(Dirpath)
        self.root_path=Dirpath
        filter = ['*.xls','*.xlsx']
        # Model
        self.dirModel = FileTreeSelectorModel(rootpath=self.root_path)
        self.dirModel.setNameFilters(filter)
        self.dirModel.setNameFilterDisables(0)
        self.dirModel.setReadOnly(False)
        self.dirModel.setRootPath(QDir.rootPath())
        root_index = self.dirModel.index(self.root_path).parent()
        self.proxy = ProxyModel(self.dirModel)
        self.proxy.setSourceModel(self.dirModel)
        self.proxy.root_path = self.root_path
        self.tree.setModel(self.proxy)
        proxy_root_index = self.proxy.mapFromSource(root_index)
        self.tree.setRootIndex(proxy_root_index)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)
        self.tree.setHeaderHidden(True)
        self.tree.clicked.connect(self.tree_click)

    @pyqtSlot(QModelIndex)
    def tree_click(self, index):
        global Filepath,Filename
        ix = self.proxy.mapToSource(index)
        Filepath = ix.data(QFileSystemModel.FilePathRole)
        Filename = ix.data(QFileSystemModel.FileNameRole)

    def initFixtureSourece(self):
        username = os.environ['USERNAME']
        sourcePath='C:/Users/'+username+'/cypress/fixtures'
        self.source_path = sourcePath
        self.dirModel2 = FileTreeSelectorModel(rootpath=self.source_path)
        self.dirModel2.setRootPath(QDir.rootPath())
        self.dirModel2.setReadOnly(False)
        root_index = self.dirModel2.index(self.source_path).parent()
        self.proxy2 = ProxyModel(self.dirModel2)
        self.proxy2.setSourceModel(self.dirModel2)
        self.proxy2.root_path = self.source_path
        self.tree2.setModel(self.proxy2)
        proxy_root_index = self.proxy2.mapFromSource(root_index)
        self.tree2.setRootIndex(proxy_root_index)
        self.tree2.setColumnHidden(1, True)
        self.tree2.setColumnHidden(2, True)
        self.tree2.setColumnHidden(3, True)
        self.tree2.setHeaderHidden(True)
        self.tree2.expandAll()
    # #编辑用例 树框中的数据
    def rightClickMenu1(self,position1):
        try:
            menu = QMenu(self.tree)
            item = self.tree.indexAt(position1)
            if os.path.isdir(Filepath):
                menu.addAction('重命名文件夹')
                menu.addAction('新增文件')
                action = menu.exec_(self.tree.mapToGlobal(position1))
                if action.text() == '重命名文件夹':
                    self.tree.edit(item)
                else:
                    fileNum = createNewFile(Filepath)
                    print(fileNum)

            else:
                menu.addAction('重命名文件')
                menu.addAction('删除文件')
                action = menu.exec_(self.tree.mapToGlobal(position1))
                if action.text() == '重命名文件':
                    self.tree.edit(item)
                else:
                    os.remove(Filepath)

        except Exception as e:
            print(e)
    # # 编辑po公共参数 树框中的数据
    # def rightClickMenu2(self,position2):
    #     try:
    #         item2 = self.tree2.currentItem()
    #         self.contextMenu = QMenu(self.tree)
    #         if item2.parent() == None:
    #             self.actionE = self.contextMenu.addAction(u'增加')
    #             self.actionE.triggered.connect(self.actionAddHandler)
    #             self.contextMenu.exec_(self.tree2.mapToGlobal(position2))
    #             self.contextMenu.show()
    #         else:
    #             self.actionF = self.contextMenu.addAction(u'删除')
    #             self.actionF.triggered.connect(self.actionMoveHandler)
    #             self.contextMenu.exec_(self.tree2.mapToGlobal(position2))
    #             self.contextMenu.show()
    #
    #
    #     except Exception as e:
    #         print(e)
    #
    #向用例树中添加测试文件
    def actionAddFileHandler(self):
        pass


    #重命名用例树中选定的文件
    def actionRenameFileHandler(self):
        pass

    #删除用例树中不需要的用例
    def actionMoveHandler(self):
        print(self.tree.currentItem().text(0))
        item = self.tree.currentItem()
        for i in range(0, item.childCount()):
            print(item.child(item.childCount() - 1).text(0))
            item.removeChild(item.child(item.childCount() - 1))
    # #删除公共参数 框中的文件
    # def actionMoveHandler2(self):
    #     print(self.tree2.currentItem().text(0))
    #     item2 = self.tree2.currentItem()
    #     for i in range(0, item2.childCount()):
    #         print(item2.child(item2.childCount() - 1).text(0))
    #         item2.removeChild(item2.child(item2.childCount() - 1))






