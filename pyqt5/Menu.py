# ****
# 菜单栏(QMenu)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Menu(QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        bar = self.menuBar()
        file = bar.addMenu('文件')
        file.addAction('新建文件夹')
        addSuit =QAction('新建TestSuit',self)
        addSuit.setShortcut("Ctrl + T")
        save = QAction("保存",self)
        save.setShortcut("Ctrl + S")
        file.addAction(save)
        file.addAction(addSuit)
        save.triggered.connect(self.process)

    def process(self,a):
        print(self.sender().text())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())