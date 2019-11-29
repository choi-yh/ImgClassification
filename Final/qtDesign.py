from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import glob


# qt designer 로 만든 gui 불러오기
form_class = uic.loadUiType("C:\\Users\\HYO\\Anaconda3\\Lib\\site-packages\\PyQt5\\uic\\window.ui")[0] # [0]을 마지막에 붙여줘야 함


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.openDir)
        self.actionExit.triggered.connect(qApp.quit) # quitAction
        self.comboBox.currentIndexChanged.connect(self.imgPreview)

    # 폴더 불러와서 comboBox 에 파일 이름 표시
    def openDir(self):
        dname = str(QFileDialog.getExistingDirectory(self, "Select Directory")) # dir 폴더 불러오기
        self.dir_path = glob.glob(dname + '/*.jpg', recursive=True) # 이미지 파일들 경로

        self.save = dname + '/Find'

        # 불러온 뒤 comboBox 에 삽입
        self.comboBox.clear()
        self.comboBox.addItems(self.dir_path) # 경로에 있는 파일 이름 추가

    # comboBox 에서 선택할 때마다 이미지 보여줌
    def imgPreview(self):
        self.fname = self.comboBox.currentText() # comboBox 에서 선택할 때마다

        # 이미지 프리뷰
        pixmap = QPixmap(self.fname).scaled(782, 458) # 이미지 불러와서 label 사이즈만큼 이미지 크기 조절
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.resize(800, 600) # window 크기 조절


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
