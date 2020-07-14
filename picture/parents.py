from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtCore

class MyCompleter(QCompleter):
    insertText = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        keywords_list = ['open browser', 'click', 'input text', 'contain', 'log', 'clear',
                         'clearcookies', 'double click', 'scrol to view', 'should', 'reload',
                         'and', 'wait', 'children', 'right click', '.rightclick()', 'read file'
            , 'equal']
        imagename_list = []
        QCompleter.__init__(self,keywords_list,imagename_list, parent)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.highlighted.connect(self.setHighlighted)
    def setHighlighted(self, text):
        self.lastSelected = text

    def getSelected(self):
        return self.lastSelected