import xlrd
import os
import itertools
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
            sourcePath = 'D:\\log\\new1.xls'
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
    def getRowContains(self,testname,ColNum):
        RowNum = 0
        try:
            rowCount = 0
            rowCount = self.get_lines()
            for RowNum in range(0, rowCount):
                if self.get_cell_data(RowNum,ColNum) == testname:
                    break
        except:
            self.log.error("Row contains check failed")
        return RowNum
    #返回用例名称对应步骤的最后一行
    def getTestStepsCount(self,testname,stepstart):
        try:
            i=0
            rowCount = self.get_lines()
            casenamelist = self.getTestCaseName()
            for i in range(stepstart, rowCount):
                for casename in casenamelist:
                    if str(testname) != casename:
                        return i+1
        except:
            self.log.error("Failed to get steps count")
            return 0
    #获取用例迭代次数
    def getTestIterations(self):
        iterate = 0
        try:
            caselist = self.getTestCaseName()
            caselist.sort()
            l=[]
            it = itertools.groupby(caselist)
            for k,g in it:
                l.append(k)
            iterate = len(l)
            if iterate >0:
                return iterate
            else:
                return 1
        except Exception as e:
            return 1

if __name__=='__main__':
    read_data = OperaExcel()
    testname ='new2'
    print(read_data.getTestStepsCount(testname,4))
