import xlrd
import os
from utils.custom_logger import  customLogger as lg
import logging
from utils.Constants import Constants
class OperaExcel:
    log = lg.log_utility(logging.DEBUG)
    constants = Constants()
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
        try:
            lines = self.get_sheet().nrows
            return lines
        except:
            self.log.error('Failed to get row count')
    #获取单元格内容
    def get_cell_data(self,row,colx):
        try:
            data = str(self.get_sheet().cell(row, colx).value)
            return data
        except:
            self.log.error("Failed to get cell data: " + str(row,colx))
    #返回测试用例名称
    def getTestCaseName(self):
        try:
            case_name = []
            lines = self.get_sheet().nrows
            for line in range(0,lines):
                test_case_name = str(self.get_sheet().cell(line, 0).value)
                if test_case_name !=None:
                    case_name.append(test_case_name)
            return case_name
        except:
            self.log.error("Failed to get testcase name")
    #返回用例执行第一步的行号


if __name__=='__main__':
    read_data = OperaExcel()
    print(read_data.getTestCaseName())
