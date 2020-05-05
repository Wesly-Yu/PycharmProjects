#coding='utf-8'

s = 0 #设置全局变量
def createCounter():
    def counter():
        global s #引用全局变量
        s = s+1
        return s
    return counter


