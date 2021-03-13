import os
import logging
from  Base.buildPythonScript import bulidPythonScript
from  Base.modifyLocator import modify_locator
from pathlib import Path

class ActionMethod():
    logging.info("执行关键字识别")
    def execute_keyword(self,projectPath,packageName,caseName,keyword,*args):
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
            modify_element = modify_locator(element)
            times= args[1]
            writeKeyWord="self.page.querySelector("+modify_element+").scrollIntoViewIfNeeded()"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '存在':
            element = args[0]
            modify_element = modify_locator(element)
            times = args[1]
            writeKeyWord = "self.page.querySelector(" + modify_element + ").waitForElementState('visible', " + times + ")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == '获取文本':
            element = args[0]
            modify_element = modify_locator(element)
            returnResult=args[1]
            writeKeyWord =returnResult+"=self.page.querySelector("+modify_element+").textContent()"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == '打印':
            element = args[0]
            writeKeyWord ="print("+element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == '切换':

        elif str(keyword) == '点击截图':

        elif str(keyword) == '上一步':
            writeKeyWord = "self.page.goBack()"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        else:
            print("无法执行没有的关键字")
            logging.info("无法执行没有的关键字")

