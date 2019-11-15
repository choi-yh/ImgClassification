import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

file = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg') # 폴더 불러오기
print(file)

tmpList = []

for tmp in file:
    tmp = tmp.replace('\\', '/')  # 경로 명칭 수정
    img = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (400, 400))
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = clahe.apply(img)
    tmpList.append(img)

print(tmpList)
