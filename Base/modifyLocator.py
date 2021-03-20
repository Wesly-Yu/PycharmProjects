def modify_locator(elementPath):
    if elementPath.find('"'):
        newPath=elementPath.replace('"',"'")
        return newPath

def define_element(element):
    if  "#" in element:
        print("id")
        return True
    elif  "." in element:
        print("class")
        return True
    elif  "@" in element:
        print("name")
        return True
    else:
        return False





if __name__ == '__main__':
    element="#myclass"
    new=modify_locator(element)
    print(new)




