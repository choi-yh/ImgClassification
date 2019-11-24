import sys
from PyQt5.QtWidgets import *


class Image(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pushButton = QPushButton("file open")
        self.pushButton.clicked.connect(self.openFile)

        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowTitle('Image Classification')
        self.setGeometry(300, 300, 600, 400)
        self.show()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        # folder = str(QFileDialog.getExistingDirectory(self, "Select Directory", './'))
        self.label.setText(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Image()
    sys.exit(app.exec_())