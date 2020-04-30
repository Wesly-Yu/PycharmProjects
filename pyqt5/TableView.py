# ****
# 工具栏(QTabelView)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QtTableView(QWidget):
    def __init__(self,arg=None):
        super(QtTableView, self).__init__(arg)
        self.setWindowTitle("表格")
        self.resize(500,600)
        self.model = QStandardItemModel(6,4)
        # self.model.setHorizontalHeaderLabels(['','','',''])
        self.tableview=QTableView()
        self.tableview.setModel(self.model)
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


QTableWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtTableView()
    main.show()
    sys.exit(app.exec_())