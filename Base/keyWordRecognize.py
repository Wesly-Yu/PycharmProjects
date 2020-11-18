from  Base.heliumMethod import *



def execute_keyword(keyword,*args):
    if str(keyword)== '打开':
        visit(args[0])
    elif str(keyword)== '点击':
        clicktext(args[0])
    elif str(keyword)== '等待':
        print(wait(args[0]))
        wait(args[0])
    elif str(keyword)== '输入':
        print(write(args[0]))
        write(args[0])
    elif str(keyword)== '下滑':
        scroll_down(args[0])
    elif str(keyword)== '存在':
        containText(args[0])
    else:
        kill_browser()
