

def increaseNum():
    f_out = open('num.txt','r+')
    a=f_out.read()
    a=int(a)+1
    print(a)
    f_out.seek(0)#清除内容
    f_out.truncate()

    f_out.write(str(a))
    f_out.close()