# ****
# 工具栏(QTabelView)
# ****
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import xlrd
class QtTableView(QWidget):
    def __init__(self,arg=None):
        super(QtTableView, self).__init__(arg)
        self.setWindowTitle("表格")
        self.resize(800,600)
        self.table=QTableWidget(8,8)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.read_excel()




    def read_excel(self):
        data = xlrd.open_workbook('./test2.xlsx')
        worksheet1 = data.sheet_by_name(u'Sheet1')
        table = data.sheet_by_index(0)
        cols = table.ncols  # 列
        rows = table.nrows  # 行
        for i in range(rows):
            rowlist = worksheet1.row_values(i)
            for j in range(len(rowlist)):
                row = self.table.rowCount()
                self.table.insertRow(row)
                if type(rowlist[j]).__name__ =='float':
                    rowlist[j] = int(rowlist[j])
                    rowlist[j] = str(rowlist[j])
                newItem = QTableWidgetItem(rowlist[j])
                self.table.setItem(i,j,newItem)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtTableView()
    main.show()
    sys.exit(app.exec_())