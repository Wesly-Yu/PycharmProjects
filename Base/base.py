import os
from utils.custom_logger import  customLogger as lg
import logging
class ActionMethod:
    log = lg.log_utility(logging.INFO)
    def execute_keyword(self,keyword,*args):
        url = str(args[0])
        print(url)
        writeKeyWord=None
        element = None
        if str(keyword).lower()=='open browser':
            writeKeyWord = "cy.visit("+"'"+url+"'"+")"
        elif str(keyword).lower() == 'click':
            #''''''等待元素显示的默认时间是10秒''''''
            element = args[0]
            timeout = args[1]
            timeout = str(timeout)
            if timeout is None:
                timeout=10000
            writeKeyWord ="cy.get("+"'"+element+"'"+",{timeout:"+timeout+"}).click()"
        elif str(keyword).lower() == 'input text':
            element = args[0]
            context =str(args[1])
            writeKeyWord = "cy.get("+"'"+element+"'"+").type("+"'"+context+"'"+")"
        elif str(keyword).lower() == 'contain':
            element = args[0]
            identify = str(args[1])
            writeKeyWord = "cy.get(" + "'" + element + "'" + ").contain(" + "'" + identify + "'" + ")"
        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")


