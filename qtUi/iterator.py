from PyQt5.Qt import *
import sys
from picture.read_txt import syntax

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit的学习")
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        self.plainTextEdit = QPlainTextEdit(self)
        self.highlight = syntax.PythonHighlighter(self.plainTextEdit.document())
        self.plainTextEdit.setFont(QFont("Microsoft YaHei", 17))
        self.plainTextEdit.resize(300, 300)
        self.plainTextEdit.move(100, 100)
        text = self.plainTextEdit.toPlainText()  # 原始的字符串
        lines_last_words = text.split("\n")[-1].split(" ")[-1]
        print(lines_last_words)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
