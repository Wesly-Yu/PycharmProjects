#coding='utf-8'
from utils.ReadExcel import OperaExcel
from Base.base import ActionMethod
from utils.CreateJsFile import WriteJsTestFileHead,WriteJsTestFileTail
from utils.custom_logger import customLogger as lg
import logging
import  pytest
class TestCase:

    log = lg.log_utility(logging.INFO)
    @pytest.fixture(autouse=True)
    def __init__(self, parent=None):
        super(TestCase, self).__init__(parent)
        self.handle_excel = OperaExcel()
        self.action_method = ActionMethod()
        keyword = self.handle_excel.get_cell(0, 0)
    def run_main(self):
        case_lines = self.handle_excel.get_lines()
        for i in  range(1,case_lines):
            method = self.handle_excel.get_cell(i,0)

if __name__ == '__main__':
    test = TestCase()
    test.run_main()