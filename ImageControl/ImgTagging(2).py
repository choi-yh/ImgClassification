# piexif 사용

import glob
import cv2
import piexif


dir_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg') # 사진 폴더 읽기
test1 = 'C:/Users/HYO/Desktop/sample/20190815_112658.jpg'  # gps 정보 없음 / Image 정보랑 EXIF 정보만 있음
test2 = 'C:/Users/HYO/Desktop/sample/20190803_183815.jpg'  # gps 정보 있음 / Image, GPS, EXIF


# 이미지 보기
def imgShow(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (400, 400))
    cv2.imshow(path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


# gps 태그 입력해서 이미지 저장하기

tag1 = getTag(test1) # 전체 태그
tag1gps = getGps(test1) # GPS 태그

tag2 = getTag(test2) # 전체 태그
tag2gps = getGps(test2) # GPS 태그

print(tag1)
print(tag2)
print(tag1gps)


# # gps 태그 입력해서 이미지 저장하기
tag1["GPS"] = tag2gps
print(tag1["GPS"])
# exif_bytes = piexif.dump(tag1)
# piexif.insert(exif_bytes, test1) # 수정된 태그 입력 (바로 입력되서 꼭 복사본 만들어서 쓰자)