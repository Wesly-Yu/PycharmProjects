import os
from utils.custom_logger import  customLogger as lg
import logging
from utils.CreateJsFile import WriteJsTestSteps
class ActionMethod:
    log = lg.log_utility(logging.INFO)
    def execute_keyword(self,file_path,testfilename,keyword,*args):
        newTestFileName = testfilename + '.js'
        createFile = file_path + '\\' + newTestFileName

        writeKeyWord=None
        element = None
        if str(keyword).lower()=='open browser':
            url = str(args[0])
            writeKeyWord = "cy.visit("+"'"+url+"'"+")"
            WriteJsTestSteps(file_path,testfilename,writeKeyWord)
        elif str(keyword).lower() == 'click':
            #''''''等待元素显示的默认时间是10秒''''''
            element = args[0]
            timeout = args[1]
            timeout = str(timeout)
            if timeout is None:
                timeout=10000
            writeKeyWord ="cy.get("+"'"+element+"'"+",{timeout:"+timeout+"}).click()"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() == 'input text':
            element = args[0]
            context =str(args[1])
            writeKeyWord = "cy.get("+"'"+element+"'"+").type("+"'"+context+"'"+")"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() == 'contain':
            element = args[0]
            identify = str(args[1])
            writeKeyWord = "cy.get(" + "'" + element + "'" + ").contain(" + "'" + identify + "'" + ")"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() == 'log':
            context = str(args[1])
            if context.startswith("#"):
                writeKeyWord = "cy.log(" +context +")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)
            else:
                writeKeyWord = "cy.log(" + "'" + context + "'" + ")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() =='clear':
            element = args[0]
            writeKeyWord = "cy.get(" + "'" + element + "'" + ").clear"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() =='clearcookies':
            writeKeyWord = "cy.clearCookies()"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() =='double click':
            element = args[0]
            writeKeyWord = "cy.get("+"'"+element+"'"+").dblclick()"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() =='scrol to view':
            element = args[0]
            writeKeyWord = "cy.get("+"'"+element+"'"+").scrollIntoView()"
            WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        elif str(keyword).lower() =='should':
            element = args[0]
            asset = args[1]
            asset_text = args[2]
            if asset_text ==None:
                writeKeyWord = "cy.get("+"'"+element+"'"+").should("+"'"+asset+"'"+")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)
            else:
                writeKeyWord = "cy.get(" + "'" + element + "'" + ").should(" + "'" + asset + "'"+"," + "'" + asset_text + "'"+")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)

        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")


