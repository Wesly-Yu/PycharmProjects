import os
import sys

class bulidPythonScript():
    def initClassMethod(self,projectPath,packageName,browserType,execType):
        Dirpath = projectPath+"/"+packageName+".py"
        classHeader = "class" + " " + packageName + "(unittest.TestCase):"
        classInit="playwright = sync_playwright().start()"
        classBrowser="browser = playwright."+browserType+".launch("+execType+"=False)"
        classPage="page = browser.newPage()"
        with open(Dirpath, 'a+', encoding="utf-8") as f:
            f.write(classHeader+'\n')
            f.write('\t'+classInit+"\n")
            f.write('\t'+classBrowser+"\n")
            f.write('\t'+classPage+"\n")
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
        initCaseStep="playwright = sync_playwright().start()"
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


