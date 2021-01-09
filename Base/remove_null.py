with open("first_script", 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        word_list = line.split(" ")

        print(word_list)