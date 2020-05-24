#coding='utf-8'


def WriteJsTestFileHead(file_path,testfilename):
    newTestFileName = testfilename +'.js'
    createFile = file_path+'\\'+newTestFileName
    realname = testfilename.split('.')[0]
    with open(createFile,'a+') as files:
        files.seek(0)
        files.write("describe('developer',function () {"+'\n')
        files.write('\t'+'it('+realname+', function() {'+'\n')

def WriteJsTestFileTail(file_path,testfilename):
    newTestFileName = testfilename + '.js'
    createFile = file_path + '\\' + newTestFileName
    with open(createFile, 'a+') as files:
        files.write('\t'+'})'+'\n')
        files.write('})'+'\n')

if __name__ == '__main__':
    file_path = 'D:\logs'
    testfilename = 'case1'
    WriteJsTestFileHead(file_path, testfilename)
    WriteJsTestFileTail(file_path, testfilename)