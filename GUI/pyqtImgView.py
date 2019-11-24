# QPixmap 사용
# QPixmap은 지금까지 다뤘던 것들과 다르게 자체적인 위젯이 없어서 Label을 이용하여 이미지를 표현
# 각 사진마다 label을 배치해야함?

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.qPixmap = QPixmap()  # QPixmap 객체 생성
        self.qPixmap.load('C:\\Users\\HYO/Desktop\\sample\\1565835332068.jpg')  # 객체에 이미지 불러오기
        self.qPixmap = self.qPixmap.scaled(400, 400)
        print(self.qPixmap)

        imgLbl = QLabel()  # 이미지 표시할 label 생성
        imgLbl.resize(400, 400)
        imgLbl.setPixmap(self.qPixmap)  # label에 이미지 표시

        self.setWindowTitle('Window')
        self.setGeometry(300, 300, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
