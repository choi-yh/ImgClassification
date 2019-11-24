# exifread 사용 (일단 망한듯)

import glob
import cv2
import exifread
import piexif
from PIL import Image


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
    f = open(path, 'rb')  # open image file for reading (binary mode)
    tags = exifread.process_file(f)  # return exif tags
    return tags  # class 'dict'


# gps 태그만 얻기
# https://dev.to/petercour/read-exif-tags-with-python-461j
def getGps(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)  # 태그 정보 읽기 (class 'dict')
    gpsInfo = {
        'GPS GPSLatitudeRef': tags.get('GPS GPSLatitudeRef', '0'),
        'GPS GPSLatitude': tags.get('GPS GPSLatitude', '0'),
        'GPS GPSLongitudeRef': tags.get('GPS GPSLongitudeRef', '0'),
        'GPS GPSLongitude': tags.get('GPS GPSLongitude', '0')
    }
    return gpsInfo


# gps 태그 없는 사진에 gps 입력하기
def insertTag(path, gps):
    tag = getTag(path)
    gpsTag = getGps(path)
    if gpsTag == {'GPS GPSLatitudeRef': '0', 'GPS GPSLatitude': '0', 'GPS GPSLongitudeRef': '0', 'GPS GPSLongitude': '0'}:
        tag['GPS GPSLatitudeRef'] = gps['GPS GPSLatitudeRef']
        tag['GPS GPSLatitude'] = gps['GPS GPSLatitude']
        tag['GPS GPSLongitudeRef'] = gps['GPS GPSLongitudeRef']
        tag['GPS GPSLongitude'] = gps['GPS GPSLongitude']
    return tag


tag1 = getGps(test1)
tag2 = getGps(test2)

print(tag1)
print(tag2)

tmp = insertTag(test1, tag2)
print(tmp)

# gps 태그 입력해서 저장하기
im = Image.open(test1)
exif_bytes = piexif.dump(tmp)
new_file = 'C:/Users/HYO/Desktop/20190815_112658_수정.jpg'
# im.save(new_file, "jpeg", exif=exif_bytes)
