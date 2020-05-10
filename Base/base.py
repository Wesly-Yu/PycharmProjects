import os
from utils.ReadExcel import OperaExcel


class ActionMethod(OperaExcel):
    def __init__(self, parent=None):
        super(ActionMethod, self).__init__(parent)
        self.read_data = OperaExcel()
        keyword=self.read_data.get_cell(0, 0)

    def execute_keyword(self,keyword,*args):
        url = args[0]
        print(url)
        writeKeyWord=None
        element = None
        if str(keyword).lower()=='open browser':
            writeKeyWord = "cy.visit("+"'"+url+"'"+")"

        if str(keyword).lower() == 'click':
            element = args[0]
            writeKeyWord ="cy.get("+"'"+element+"'"+").click()"
