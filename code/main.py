from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QSplitter
import sys


class GUI(QWidget):

    def __init__(self):
        super().__init__()

        #   从文件中加载ui定义
        qfile = QFile("../ui/uifile.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        #   从ui定义中动态创建一个窗口对象
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.ui.show()
    sys.exit(app.exec_())
