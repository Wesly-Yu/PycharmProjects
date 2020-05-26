#coding='utf-8'


def WriteJsTestFileHead(file_path,testfilename):
    newTestFileName = testfilename +'.js'
    createFile = file_path+'\\'+newTestFileName
    realname = testfilename.split('.')[0]
    with open(createFile,'a+',encoding='utf-8') as files:
        files.seek(0)
        files.write("describe('developer',function () {"+'\n')
        files.write('\t'+'it('+'"'+realname+'"'+', function() {'+'\n')

def WriteJsTestFileTail(file_path,testfilename):
    newTestFileName = testfilename + '.js'
    createFile = file_path + '\\' + newTestFileName
    with open(createFile, 'a+',encoding='utf-8') as files:
        files.write('\t'+'})'+'\n')
        files.write('})'+'\n')
def WriteJsTestSteps(file_path,testfilename,steps):
    newTestFileName = testfilename + '.js'
    createFile = file_path + '\\' + newTestFileName
    with open(createFile, 'a+',encoding='utf-8') as files:
        files.write('\t'+'\t'+steps+'\n')


# if __name__ == '__main__':
#     file_path = 'D:\log'
#     testfilename = 'case2'
#     url="www.baicu.com"
#     steps="cy.visit("+"'"+url+"'"+")"
#     WriteJsTestFileHead(file_path, testfilename)
#     WriteJsTestSteps(file_path, testfilename, steps)
#     WriteJsTestFileTail(file_path, testfilename)