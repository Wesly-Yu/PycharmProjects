import os
import sys

class bulidPythonScript():
    def initClassMethod(self,projectPath,packageName,browserType,execType):
        Dirpath = projectPath+"/"+packageName+".py"
        importPackageOne="import unittest"
        importPackageTwo = "from time import sleep"
        importPackageThree = "from helium import *"
        importPackageFour = "from selenium.webdriver import ChromeOptions,FirefoxOptions"
        classHeader = "class" + " " + packageName + "(unittest.TestCase):"
        classInitChromeBrowser="ChromeOptions = ChromeOptions()"
        classInitFireFoxBrowser = "FireFoxOptions = FirefoxOptions()"
        classInitMaxPage="options.add_argument('--start-maximized')"
        with open(Dirpath, 'a+', encoding="utf-8") as f:
            f.write('\t' + importPackageOne + "\n")
            f.write('\t' + importPackageTwo + "\n")
            f.write('\t' + importPackageThree + "\n")
            f.write('\t' + importPackageFour + "\n")
            f.write(classHeader+'\n')
            f.write('\t'+classInitChromeBrowser+"\n")
            f.write('\t'+classInitFireFoxBrowser+"\n")
            f.write('\t' + classInitMaxPage + "\n")
    def addTailMethod(self,projectPath,packageName,caseList):
        Dirpath = projectPath + "/" + packageName + ".py"
        classMain = "if __name__ == '__main__':"
        classSuit = "suit = unittest.TestSuite()"
        with open(Dirpath, 'a+', encoding="utf-8") as f:
            f.write(classMain + '\n')
            f.write('\t'+classSuit+'\n')
            for casename in range(len(caseList)):
                case_name = caselist[casename]
                addTest="suit.addTest("+packageName+"("+"'"+case_name+"'"+"))"
                f.write('\t'+addTest+'\n')
            addRunner = "runner = unittest.TextTestRunner()"
            addSuitRunner="runner.run(suit)"
            f.write('\t'+addRunner+'\n')
            f.write('\t'+addSuitRunner+'\n')
    def addTestScriptMethod(self,projectPath,packageName,caseName,step):
        Dirpath = projectPath + "/" + packageName + ".py"
        caseNameMethod = "def"+" "+caseName+"(self):"
        with open(Dirpath, 'a+', encoding="utf-8") as f:
            f.write('\t'+caseNameMethod+'\n')
            f.write('\t'+'\t'+step+'\n')








if __name__ == '__main__':
    projectPath="/Users/yupeng55/Documents/project/PycharmProjects/Base"
    packageName="zhuangba"
    caselist=['first_script','second_script']
    bp=bulidPythonScript()
    bp.initClassMethod(projectPath,packageName,"chromium","headless")
    bp.addTailMethod(projectPath, packageName,caselist)


