from helium import *
from selenium import *
import time
from playwright import sync_playwright

#打开页面
def  visit(url):
    driver = start_firefox(url)

def wait(time):
    time.sleep(time)
#等待页面元素文字加载完成,默认等待10秒
def wait_until_text(findText):
    wait_until(Text(findText).exists())
#点击操作
def clicktext(element):
    click(Text(element))
#不需要切换 iframe，直接输入
def input_value(inputText,locator):
    write(inputText,into=locator)

def write(text):
    write(text)
#拖动
def hdrag(elementone,elementwo):
    drag(elementone,to=elementwo)

#向下滚动像素，默认100个像素
def scroll_down():
    scroll_down()

#向上滚动，默认100个像素
def scroll_up():
    scroll_up()

#向右滚动
def scroll_right():
    scroll_right()

#选择框中选择元素
def selectFromComboBox(element,value):
    select(element,value)

#拖动文件到指定的元素上
def dragFile(filePath,element):
    drag_file(filePath,to=element)

#刷新页面
def reflesh():
    refresh()
#让您识别网页上的任何文本或标签。这对于检查特定文本是否存在非常有用
def containText(findtext):
    Text(findtext).exists()

#让你识别一个网页上的列表项(HTML <li>元素)。这在与导航栏的元素交互时通常很有用
def clickListItem(text):
    click(ListItem(text))

#点击包含指定text的按钮
def clickButton(text):
    click(Button(text))

#点击text复选框
def clickCheckBox(text):
    click(CheckBox(text))
#点击接受 alert弹窗
def acceptAlert():
    Alert.accept()

def dismissAlert():
    Alert.dismiss()

#获取指定文本元素的值
def  getTextFiled(targetText):
    TextField(targetText).value()

#切换窗口
def switchTo(title):
    switch_to(title)


#关闭浏览器
def kill_browser():
    kill_browser()
