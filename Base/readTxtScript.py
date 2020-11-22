# def getQplainTextEdit(scriptfilename):
from Base.keyWordRecognize import execute_keyword

#path  Only for Mac  system#
#crntDir = "/Users/yupeng55/Documents/pythonProject1/UiTest/"
#list_data = crntDir + "first_script"

def  test_excution():
    with open("first_script",'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            word_list = line.split(" ")
            while '' in word_list:
                word_list.remove('')
            key_words = word_list[0]
            if len(word_list)==1:
                execute_keyword(key_words)
            else:
                paramone = word_list[1]
                execute_keyword(key_words, paramone)




if __name__ == '__main__':
    test_excution()
