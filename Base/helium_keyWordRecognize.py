import os
import logging
from  Base.buildPythonScript import bulidPythonScript
from  Base.modifyLocator import modify_locator
from getConfig import *


class ActionMethod():
    logging.info("执行关键字识别")
    def execute_keyword(self,projectPath,packageName,caseName,keyword,*args):
        if str(keyword)== '打开':
            if browser=="chrome":
                url = str(args[0])
                head=cf.get('Options', 'headless')
                writeKeyWord = "start_chrome("+url+",options=self.ChromeOptions,headless="+head+")"
                bulidPythonScript.addTestScriptMethod(projectPath,packageName,caseName,writeKeyWord)
            else:
                url = str(args[0])
                head=cf.get('Options', 'headless')
                writeKeyWord = "start_firefox("+url+",options=self.FireFoxOptions,headless="+head+")"
                bulidPythonScript.addTestScriptMethod(projectPath,packageName,caseName,writeKeyWord)
        elif str(keyword)== '点击':
            element=str(args[0])
            modify_element=modify_locator(element)
            writeKeyWord ="click("+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '等待':
            time = str(args[0])+"000"
            writeKeyWord = "sleep("+time+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '输入':
            element=args[0]
            modify_element = modify_locator(element)
            inputString=str(args[1])
            writeKeyWord = "write("+inputString+", into="+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '上滑':
            pix= args[0]
            writeKeyWord="scroll_up(num_pixels="+pix+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== '下滑':
            pix = args[0]
            writeKeyWord = "scroll_down(num_pixels="+pix+")"
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

