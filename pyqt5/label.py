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
        layout=QVBoxLayout()
        self.label = QLabel('请选择浏览器')
        self.cb=QComboBox()
        self.cb.addItem('Chrome')
        self.cb.addItem('Firefox')
        self.cb.addItems(['Opera','Edge','Chromium','Canary','Electron'])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)
    def selectionChange(self,index):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        # for count in range(self.cb.count()):
        #     print('item'+str(count)+'='+self.cb.itemText(count))
        print('Current index is:', index, 'Current selected is:' + self.cb.currentText())
if __name__=='__main__':
    app =QApplication(sys.argv)
    main = QcomboBoxSelect()
    main.show()
    sys.exit(app.exec_())