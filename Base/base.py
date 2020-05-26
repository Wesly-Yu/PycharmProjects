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
            print('+\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\+')
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
            if context.split('#')[1] !=None:
                writeKeyWord = "cy.log(" +context +")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)
            else:
                writeKeyWord = "cy.log(" + "'" + context + "'" + ")"
                WriteJsTestSteps(file_path, testfilename, writeKeyWord)
        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")


