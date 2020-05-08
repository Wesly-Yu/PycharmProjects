import os
import re




def createNewFile(path):
    filenamedict = []
    root=None
    path ='D:\log'
    for root, dirs, files in os.walk(path):
        for file in files:
            filenamedict.append(file)
    ret = re.findall('(?<=new)(\d)(?=.xls)',str(filenamedict))
    filenumber = int(ret[-1])+1
    return filenumber




