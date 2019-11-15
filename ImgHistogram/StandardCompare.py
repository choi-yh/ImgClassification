import glob
import cv2
import matplotlib.pyplot as plt
import random

file_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg') # 폴더 불러오기
tmp = file_path[17]


# 이미지 히스토그램
def histogram(image):
    image = image.replace('\\', '/') # 경로 에러 변경
    image = cv2.imread(image, cv2.IMREAD_COLOR) # 흑백 이미지로 출력하기
    image = cv2.resize(image, (400, 400)) # 이미지 크기 조절

    # histogram 출력하기
    hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    return hist, image


# 히스토그램 면적 차이 계산
def compare(a, b):
    result = 0
    for i in range(255):
        result += (a[i] - b[i]) ** 2  # trapezoidal
    return result


# 유사한 이미지
hist1, im1 = histogram(tmp)
hist2, im2 = histogram(file_path[200])


plt.subplot(221)
plt.imshow(im1)
plt.subplot(222)
plt.plot(hist1)

plt.subplot(223)
plt.imshow(im2)
plt.subplot(224)
plt.plot(hist2)

plt.show()

print(compare(hist1, hist2))


# 다른 이미지
hist3, im3 = histogram(tmp)
hist4, im4 = histogram(file_path[50])


plt.subplot(221)
plt.imshow(im3)
plt.subplot(222)
plt.plot(hist3)

plt.subplot(223)
plt.imshow(im4)
plt.subplot(224)
plt.plot(hist4)

plt.show()

print(compare(hist3, hist4))
