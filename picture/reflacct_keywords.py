def execute_keyword(keyword,*args):
    if str(keyword)== '打开':
        print("执行打开命令")
    elif str(keyword)== '点击':
        print("执行点击命令")
    elif str(keyword)== '等待':
        print("执行等待命令")
    elif str(keyword)== '输入':
        print("执行输入命令")
    elif str(keyword)== '滑动':
        print("执行滑动命令")
    elif str(keyword)== '存在':
        print("执行断言命令")
    else:
        print("没有这个关键字执行，退出driver")