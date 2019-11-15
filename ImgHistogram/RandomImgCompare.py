import glob
import cv2
import matplotlib.pyplot as plt
import random

file_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg')  # 폴더 불러오기
tmp = file_path[17]


# 이미지 히스토그램
def histogram(image):
    image = image.replace('\\', '/') # 경로 에러 변경
    image = cv2.imread(image, cv2.IMREAD_COLOR)  # 흑백 이미지로 출력하기
    image = cv2.resize(image, (400, 400))  # 이미지 크기 조절

    # histogram 출력하기
    hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    return hist, image


# 히스토그램 면적 차이 계산
def compare(a, b):
    result = 0
    for i in range(255):
        result += (a[i] - b[i]) ** 2  # trapezoidal
    return result


# 랜덤 이미지 3개 추출해서 히스토그램이랑 보여주기
sample = random.sample(file_path, 3)
res = [[], [], []]

for i in range(3):
    hist, im = histogram(sample[i])
    plt.subplot(121)
    plt.imshow(im)

    plt.subplot(122)
    plt.plot(hist)
    plt.show()

    for j in range(len(file_path)):
        compHist, compImg = histogram(file_path[j])
        if compare(hist, compHist) < 2e+08:
            res[i].append(compImg)
print(res)
print(len(res[0]), len(res[1]), len(res[2]))