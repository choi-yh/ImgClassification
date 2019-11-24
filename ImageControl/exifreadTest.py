import glob
import cv2
import random
import exifread

dir_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg') # 사진 폴더 읽기
# test = random.choice(dir_path) # 랜덤 사진 테스트
test1 = 'C:/Users/HYO/Desktop/sample/20190815_112658.jpg' # gps 정보 없음
test2 = 'C:/Users/HYO/Desktop/sample/20190803_183815.jpg' # gps 정보 있음


# 이미지 보기
def imgShow(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (400, 400))
    cv2.imshow(path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# https://dev.to/petercour/read-exif-tags-with-python-461j
def process_img(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f) # 태그 정보 읽기 (class 'dict')
    info = {
        'Image DateTime': tags.get('Image DateTime', '0'), # 사진 찍은 날짜
        'GPS GPSLatitudeRef': tags.get('GPS GPSLatitudeRef', '0'),
        'GPS GPSLatitude': tags.get('GPS GPSLatitude', '0'),
        'GPS GPSLongitudeRef': tags.get('GPS GPSLongitudeRef', '0'),
        'GPS GPSLongitude': tags.get('GPS GPSLongitude', '0')
    }
    return info


def getGps(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f) # 태그 정보 읽기 (class 'dict')
    gpsInfo = {
        'GPS GPSLatitudeRef': tags.get('GPS GPSLatitudeRef', '0'),
        'GPS GPSLatitude': tags.get('GPS GPSLatitude', '0'),
        'GPS GPSLongitudeRef': tags.get('GPS GPSLongitudeRef', '0'),
        'GPS GPSLongitude': tags.get('GPS GPSLongitude', '0')
    }
    return gpsInfo


imgShow(test1)
imgShow(test2)

inf1 = process_img(test1)
inf2 = process_img(test2)
print(inf1)
print(inf2)
