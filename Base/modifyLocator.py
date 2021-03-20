def modify_locator(elementPath):
    if elementPath.find('"'):
        newPath=elementPath.replace('"',"'")
        return newPath



