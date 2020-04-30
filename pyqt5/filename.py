import os


def file_name(path):
    return os.listdir(path)


if __name__ == "__main__":
    path = 'C:\\Users\\...\\Desktop\\SeeTheData'
    dirs = file_name(path)
    for i in dirs:
        print(i)