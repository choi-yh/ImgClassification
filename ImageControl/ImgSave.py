# 찾은 이미지 이름 변경하고 태그 달아서 저장하기

import os
import cv2
import piexif
import glob


# 전체 태그 얻기
def getTag(path):
    tags = piexif.load(path)  # return exif tags
    return tags  # class 'dict'


# gps 태그만 얻기
def getGps(path):
    tags = piexif.load(path)  # 태그 정보 읽기 (class 'dict')
    gpsInfo = {
        1: tags["GPS"].get(1, '0'),
        2: tags["GPS"].get(2, '0'),
        3: tags["GPS"].get(3, '0'),
        4: tags["GPS"].get(4, '0')
    }
    return gpsInfo


# 찾은 파일들을 폴더 생성해서 새로 저장
def _createFolder(directory='C:\\Users\\HYO\\Desktop/find'):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def save(path, image):
    tmp = path.find('/')
    newPath = save_dir + path[tmp:]
    cv2.imwrite(newPath, image)
    return newPath


save_dir = 'C:\\Users\\HYO\\Desktop\\find'


dir_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg')
test = 'C:\\Users\\HYO\\Desktop\\sample/20190803_172326.jpg'

tmp = test.find('/')

img = cv2.imread(test, cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400)) # resize 하면 태그정보 사라짐

tag = getTag(test)
exif_bytes = piexif.dump(tag)

_createFolder(save_dir)
nPath = save(test, img)
piexif.insert(exif_bytes, nPath)

