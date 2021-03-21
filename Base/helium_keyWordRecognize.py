import os
import logging
from  Base.buildPythonScript import bulidPythonScript
from  Base.modifyLocator import modify_locator,define_element,text_add_quotation
from getConfig import *


class ActionMethod():
    logging.info("执行关键字识别")
    def execute_keyword(self,projectPath,packageName,caseName,keyword,*args):
        if str(keyword)== 'open':
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
        elif str(keyword)== 'click':
            element=str(args[0])
            modify_element=modify_locator(element)
            writeKeyWord ="click("+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== 'click button':
            element=str(args[0])
            modify_element=modify_locator(element)
            writeKeyWord ="click(Button("+modify_element+"))"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== 'wait':
            time = str(args[0])
            writeKeyWord = "sleep("+time+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== 'write':
            Text=args[0]
            element = str(args[1])
            if define_element(element)==True:
                writeKeyWord = "write("+Text+", into=S("+element+"))"
                bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
            else:
                writeKeyWord = "write(" + Text + ", into="+element+")"
                bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== 'scroll up':
            pix= args[0]
            writeKeyWord="scroll_up(num_pixels="+pix+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword)== 'scroll down':
            pix = args[0]
            writeKeyWord = "scroll_down(num_pixels="+pix+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'press':
            element = str(args[0])
            writeKeyWord ="press("+element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'print':
            element = args[0]
            writeKeyWord ="print("+element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'doubleclick':
            element = args[0]
            modify_element = modify_locator(element)
            writeKeyWord = "doubleclick("+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'rightclick':
            element = args[0]
            modify_element = modify_locator(element)
            writeKeyWord = "rightclick("+modify_element+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'select':
            element = args[0]
            element2=args[1]
            modify_element1 = modify_locator(element)
            modify_element2 = modify_locator(element2)
            writeKeyWord = "select("+element+", "+element2+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'attach_file':
            element = args[0]
            element2=args[1]
            writeKeyWord = "attach_file("+element+", to="+element2+")"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'refresh':
            writeKeyWord = "refresh()"
            bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'wait_until':
            element = args[0]
            element2=args[1]
            check_result=define_element(element)
            if check_result==False:
                if element!=None:
                    text=text_add_quotation(element)
                    writeKeyWord = "wait_until(Text("+text+").exists)"
                    bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
                else:
                    print("Text parameter is None")
            else :
                modify_element1 = modify_locator(element)
                if element2=="":
                    writeKeyWord = "wait_until(S("+modify_element1+").exists)"
                    bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
                else:
                    writeKeyWord = "wait_until(S("+modify_element1+").exists,"+element2+")"
                    bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
        elif str(keyword) == 'exists_text':
            element = args[0]
            if element!="":
                text=text_add_quotation(element)
                writeKeyWord = "Text("+text+").exists()"
                bulidPythonScript.addTestScriptMethod(projectPath, packageName, caseName, writeKeyWord)
            else:
                logging.error("please input your text")
        else:
            print("无法执行没有的关键字")
            logging.info("无法执行没有的关键字")

