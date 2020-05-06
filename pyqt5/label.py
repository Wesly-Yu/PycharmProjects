# ****
# 下拉列表(QComboBox)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QcomboBoxSelect(QWidget):
    def __init__(self):
        super(QcomboBoxSelect,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表')
        self.resize(300,150)

if __name__=='__main__':
    app =QApplication(sys.argv)
    main = QcomboBoxSelect()
    main.show()
    sys.exit(app.exec_())