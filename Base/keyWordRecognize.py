import os
import logging
from  Base.buildPythonScript import bulidPythonScript
from  Base.modifyLocator import modify_locator

class ActionMethod():
    logging.info("执行关键字识别")
    def execute_keyword(self,projectPath,packageName,keyword,*args):
        if str(keyword)== '打开':
            url = str(args[0])
            writeKeyWord = "self.page.goto("+url+")"
            bulidPythonScript.addTestScriptMethod(projectPath,packageName,caseName,writeKeyWord)
        elif str(keyword)== '点击':
            element=str(args[0])
            modify_element=modify_locator(element)
            writeKeyWord ="self.page.click("+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '等待':
            time = str(args[0])+"000"
            writeKeyWord = "self.page.waitForTimeout("+time+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '输入':
            element=args[0]
            modify_element = modify_locator(element)
            inputString=str(args[1])
            cleanWord = "self.page.fill("+modify_element+",'')"
            writeKeyWord = "self.page.type("+modify_element+","+inputString+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, cleanWord)
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '滑动到页面中间':
            element = args[0]
            times= args[1]
            writeKeyWord=self.page.querySelector('a[name="tj_login"]').waitForElementState('visible', 5000)
        elif str(keyword)== '存在':

        elif str(keyword) == '获取文本':

        elif str(keyword) == '存在':

        else:
            print("无法执行没有的关键字")
            logging.info("无法执行没有的关键字")

