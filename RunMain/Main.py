#coding='utf-8'
from utils.ReadExcel import OperaExcel
from Base.base import ActionMethod
from utils.CreateJsFile import WriteJsTestFileHead,WriteJsTestFileTail
from utils.custom_logger import customLogger as lg
from utils.Constants import Constants
import os
class TestCase():

    log = lg.log_utility()
    # @pytest.fixture(autouse=True)
    def __init__(self, parent=None):
        global sourcePath
        username = os.environ['USERNAME']
        sourcePath = 'C:/Users/' + username + '/cypress/integration'
        super(TestCase, self).__init__()
        self.handle_excel = OperaExcel()
        self.action_method = ActionMethod()
        self.constants = Constants()
        keyword = self.handle_excel.get_cell_data(0, 0)
    def run_main(self):
        TestCase_List = []
        iterates=self.handle_excel.getTestIterations()
        testcaselists=self.handle_excel.getTestCaseName()
        for  j in testcaselists:
            if j not in TestCase_List:
                TestCase_List.append(j)
        # for iterate in range(1,iterates+1):
        #将用例列表中的 用例一一取出
        global  testcasename
        for testcasename in TestCase_List:
            WriteJsTestFileHead(sourcePath, testcasename)
            #返回用例名称对应的第一个行id
            nStartStep = self.handle_excel.getRowContains(testcasename,self.constants.Col_TestCaseID)
            # 返回用例名称对应的最后一行id
            nEndStep = self.handle_excel.getTestStepsCount(testcasename,nStartStep)
            self.log.info("*****************************************************************************************************")
            self.log.info("Test case: " + str(testcasename))
            self.log.info("************************************************************************")
            for step in range(nStartStep, nEndStep):
                nActionKeyword = self.handle_excel.get_cell_data(step,self.constants.Col_TestKeyWords)
                nElementLocator = self.handle_excel.get_cell_data(step,self.constants.Col_TestLocator)
                nElementInput = self.handle_excel.get_cell_data(step,self.constants.Col_TestInput)
                self.action_method.execute_keyword(sourcePath,testcasename,nActionKeyword,nElementLocator,nElementInput)
            WriteJsTestFileTail(sourcePath,testcasename)
            self.log.info("*********************Write JS file Success*********************")
if __name__ == '__main__':
    test = TestCase()
    test.run_main()