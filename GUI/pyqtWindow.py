import sys
from PyQt5.QtWidgets import *


class Image(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        openFolder = menubar.addMenu('&File')

        self.setWindowTitle('Image Classification')
        self.setGeometry(300, 300, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Image()
    sys.exit(app.exec_())