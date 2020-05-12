#coding='utf-8'
from utils.ReadExcel import OperaExcel
from Base.base import ActionMethod

class TestCase:
    def __init__(self, parent=None):
        super(TestCase, self).__init__(parent)
        self.handle_excel = OperaExcel()
        self.action_method = ActionMethod()
        keyword = self.handle_excel.get_cell(0, 0)
