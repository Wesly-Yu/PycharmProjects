# ****
# 工具栏(QMenu)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ToolsBar(QMainWindow):
    def __init__(self):
        super(ToolsBar, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("工具栏")
        self.resize(400,300)
        tb1 = self.addToolBar("文件")
        new = QAction(QIcon('./image/New.png'),"新建",self)
        open = QAction(QIcon('./image/Open.png'),"打开",self)
        tb1.addAction(new)
        tb1.addAction(open)
        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolsBar()
    main.show()
    sys.exit(app.exec_())