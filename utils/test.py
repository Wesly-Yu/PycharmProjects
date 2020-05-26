



def test1():
    testname='new3'
    list =['new1','new1','new1','new2','new2','new2','new3','new3']
    for i in range(6, len(list)):
        # if testname == list[-1]:
        #     return
        if testname == list[-1]:
            return len(list)-1
        elif str(testname) != str(list[i]):
            return i
        else:
            print('Fail')


if __name__=='__main__':
    test=test1()
    print(test)