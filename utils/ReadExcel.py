import xlrd
import os
class OperaExcel:

    def __init__(self,excel_path=None):
        if excel_path is None:
            username = os.environ['USERNAME']
            # sourcePath = 'C:/Users/' + username + '/cypress/fixtures/new1.xls'
            sourcePath = 'D:/logs/new1.xls'
            self.excel_path =sourcePath
        else:
            self.excel_path = excel_path
        self.excel = self.get_excel_Data()

    def get_excel_Data(self):
        tabeles = xlrd.open_workbook(self.excel_path)
        return tabeles

    #获取当前sheet号
    def get_sheet(self,sheedID=None):
        if sheedID is None:
            sheedID = 0
        sheet_data = self.excel.sheets()[sheedID]
        return sheet_data


    #获取行数
    def get_lines(self):
        lines = self.get_sheet().nrows
        return lines
    #获取单元格内容
    def get_cell(self,row,colx):
        data = self.get_sheet().cell(row,colx).value
        return data

if __name__=='__main__':
    read_data = OperaExcel()
    print(read_data.get_lines())
    print(read_data.get_cell(0,1))
