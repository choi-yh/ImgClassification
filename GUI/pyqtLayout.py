from PyQt5.QtWidgets import *
import glob

dir_path = glob.glob('C:\\Users\\yhcho\\OneDrive\\바탕 화면\\sample/*.jpg')
# dir_path = glob.glob('C:\\Users\\HYO\\Desktop\\sample/*.jpg')


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Window')
        self.setGeometry(300, 300, 800, 600)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        openMenu = fileMenu.addMenu('&Open')

        qb = QComboBox()  # 디렉토리에 있는 파일명
        qb.addItems(dir_path)
        qb.insertSeparator(10)

        button = QPushButton("Find Image")  # 실행 버튼
        label = QLabel("Image") # 이미지 보여줄 레이블

        layout = QGridLayout()

        layout.addWidget(qb, 0, 0)
        layout.addWidget(button, 1, 0)
        layout.addWidget(label, 2, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    app.exec_()