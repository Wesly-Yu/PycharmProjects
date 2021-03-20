def modify_locator(elementPath):
    if elementPath.find('"'):
        newPath=elementPath.replace('"',"'")
        return newPath

def define_element(element):
    if "#" or "@" in element:
        print(element)
        return True



if __name__ == '__main__':
    element="#username"
    define_element(element)




