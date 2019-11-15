import glob
import cv2
import matplotlib.pyplot as plt

file_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg') # 폴더 불러오기
print(file_path)
tmp = file_path[17] # test image
tmp = tmp.replace('\\', '/') # 경로 명칭 수정


# 이미지 히스토그램
def histogram(image):
    image = image.replace('\\', '/') # 경로 에러 변경
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 출력하기
    image = cv2.resize(image, (400, 400)) # 이미지 크기 조절

    # Using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image = clahe.apply(image)

    cv2.imshow('CLAHE', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # histogram 출력하기
    hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    return hist


hist = histogram(tmp)
print(type(hist), hist.shape)
print(hist)

# 히스토그램 보기
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
