import os
import cv2
import piexif
import glob
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


#####################################################
# (16, 16) 사이즈 binary image 변환
def img2hash(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (16, 16))
    avg = img.mean()  # 픽셀 평균값 구하기
    bi = 1 * (img > avg)  # 픽셀 평균값보다 큰 픽셀 갯수 구하기
    return bi


def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a != b).sum()
    return distance


# 전체 태그 얻기
def getTag(path):
    tags = piexif.load(path)  # return exif tags
    return tags # class 'dict'


# 찾은 파일들을 폴더 생성해서 새로 저장
def _createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


# 유사 이미지 찾기
def findImg(folder_path, query, save_dir):
    # 대상 이미지 불러오기
    query_img = cv2.imread(query, cv2.IMREAD_COLOR)
    query_img = cv2.resize(query_img, (400, 400)) # 이미지 사이즈 바꾸고
    query_hash = img2hash(query_img) # 해쉬 이미지로 변환

    qTag = getTag(query) # 쿼리 이미지 태그
    _createFolder(save_dir) # 저장할 폴더 생성

    for path in folder_path:
        # 이미지 읽기
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        reimg = cv2.resize(img, (400, 400))

        # 이미지 찾는 동안 띄워놓기
        cv2.imshow("Searching...", reimg)
        cv2.waitKey(5)

        # hamming distance 를 통해 비교하기
        img_hash = img2hash(reimg)
        dst = hamming_distance(query_hash, img_hash) / 256 # hamming distance 비율로 바꾸기 (0 ~ 1)

        if dst < 0.20: # hamming distance 가 80퍼 이상 유사한 이미지를 찾는다.
            print(path, dst)
            cv2.imshow(path, reimg)

            tag = getTag(path) # 유사 이미지의 태그 정보
            # gps 태그가 없는 이미지들의 태그를 저장
            if tag['GPS'] == {}:
                tag["GPS"] = qTag["GPS"]

            # 유사 이미지들을 gps태그를 수정해서 새로 저장
            # 저장할 경로로 파일 이름 변경
            tmp = path.find('\\')
            sPath = save_dir + path[tmp:]
            cv2.imwrite(sPath, img) # 새 경로로 이미지 저장

            exif_bytes = piexif.dump(tag)
            piexif.insert(exif_bytes, sPath) # 저장한 이미지에 수정된 태그 삽입

    cv2.destroyWindow("Searching...")
    cv2.destroyAllWindows()


#################################################
# qt designer 로 만든 gui 불러오기
form_class = uic.loadUiType("C:\\Users\\HYO\\Anaconda3\\Lib\\site-packages\\PyQt5\\uic\\window.ui")[0] # [0]을 마지막에 붙여줘야 함


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.openDir)
        self.actionExit.triggered.connect(qApp.quit) # quitAction
        self.comboBox.currentIndexChanged.connect(self.imgPreview)
        self.pushButton.clicked.connect(self.Find) # Find Image

    # 폴더 불러와서 comboBox 에 파일 표시
    def openDir(self):
        dname = str(QFileDialog.getExistingDirectory(self, "Select Directory")) # dir 폴더 불러오기
        self.dir_path = glob.glob(dname + '/*.jpg', recursive=True) # 이미지 파일들 경로
        self.save = dname + '\\Find'

        # 불러온 뒤 comboBox에 삽입
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

    def Find(self):
        findImg(self.dir_path, self.fname, self.save)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

