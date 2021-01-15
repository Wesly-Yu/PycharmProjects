import os
import logging
from  Base.buildPythonScript import bulidPythonScript


class ActionMethod():
    logging.info("执行关键字识别")
    def execute_keyword(self,projectPath,packageName,keyword,*args):
        if str(keyword)== '打开':
            url = str(args[0])
            writeKeyWord = "self.page.goto("+url+")"
            bulidPythonScript.addTestScriptMethod(projectPath,packageName,caseName,writeKeyWord)
        elif str(keyword)== '点击':
            element=str(args[0])
            writeKeyWord ="self.page.click("+element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '等待':
            time = str(args[0])
            writeKeyWord = "sleep("+time+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '输入':
            element=args[0]
            inputString=str(args[1])
            cleanWord = "self.page.fill("+element+",'')"
            writeKeyWord = "self.page.type("+element+","+inputString+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, cleanWord)
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '下滑':

        elif str(keyword)== '存在':

        else:
            print("无法执行没有的关键字")
            logging.info("无法执行没有的关键字")

