#coding='utf-8'
from utils.ReadExcel import OperaExcel
from Base.base import ActionMethod
from utils.CreateJsFile import WriteJsTestFileHead,WriteJsTestFileTail
from utils.custom_logger import customLogger as lg
from utils.Constants import Constants
import logging
import  pytest
class TestCase():

    log = lg.log_utility(logging.INFO)
    # @pytest.fixture(autouse=True)
    def __init__(self, parent=None):
        super(TestCase, self).__init__()
        self.handle_excel = OperaExcel()
        self.action_method = ActionMethod()
        self.constants = Constants()
        keyword = self.handle_excel.get_cell_data(0, 0)
    def run_main(self):
        iterates=self.handle_excel.getTestIterations()
        testcaselists=self.handle_excel.getTestCaseName()
        for ntestCase in range(1,iterates):
            #将用例列表中的 用例一一取出
            for testcase in testcaselists:
                # 用例名称对应的第一个行id
                nStartStep = self.handle_excel.getRowContains(testcase,self.constants.Col_TestCaseID)


if __name__ == '__main__':
    test = TestCase()
    test.run_main()