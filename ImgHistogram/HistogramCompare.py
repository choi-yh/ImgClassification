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
    # Using CLAHE
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # image = clahe.apply(image)

    # img show
    # cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # histogram 출력하기
    hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    return hist, image


# 히스토그램 면적 차이 계산
def compare(a, b):
    result = 0
    for i in range(255):
        result += (abs(a[i] - b[i]) + abs(a[i + 1] - b[i + 1])) // 2  # trapezoidal
    return result


# hist1, _ = histogram(tmp)
# hist2, _ = histogram(file_path[20])


# plt.subplot(211)
# plt.plot(hist1)
#
# plt.subplot(212)
# plt.plot(hist2)
# plt.xlim([0, 256])
#
# plt.show()
#
# print(compare(hist1, hist2))

base, _ = histogram(tmp)

for i in range(len(file_path)):
    tmp = file_path[i]
    hist, img = histogram(tmp)
    res = compare(base, hist)

    sim = []
    if res <= 5e+05:
        cv2.imshow('similar', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        sim.append(tmp)
print(sim)


# 랜덤 이미지 테스트
# ranImg = random.sample(file_path, 10)
# for item in ranImg:
#     hist, img = histogram(item)
#
#     plt.subplot(121)
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#
#     plt.subplot(122)
#     plt.plot(hist)
#     plt.xlim([0, 256])
#
#     plt.show()