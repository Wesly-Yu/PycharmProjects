def modify_locator(elementPath):
    if elementPath.find('"'):
        newPath=elementPath.replace('"',"'")
        return newPath



if __name__ == '__main__':
    locator='a[name="tj_login"]'
    result =modify_locator(locator)
    print(result)