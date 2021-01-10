from pyqt_screenshot.screenshot import Screenshot, constant
from qtUi.NewMainWindows import Ui_MainWindow
from PyQt5 import QtWidgets


class ToolsBarSlot(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(ToolsBarSlot,self).__init__(parent)
        self.setupUi(self)
        self.actionScreenShot.triggered.connect(self.TakeScreenShot)
        #self.iniUI()

    def TakeScreenShot(self):
        self.showMinimized()
        img = Screenshot.take_screenshot(constant.SAVE_TO_FILE)
        img.show()
