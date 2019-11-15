import glob
import cv2
import random
import exifread

dir_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg')
test = random.choice(dir_path)

# 이미지 보기
img = cv2.imread(test)
img = cv2.resize(img, (400, 400))
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# https://dev.to/petercour/read-exif-tags-with-python-461j
def process_img(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        'Image DateTime': tags.get('Image DateTime', '0'),
        'GPS GPSLatitudeRef': tags.get('GPS GPSLatitudeRef', '0'),
        'GPS GPSLatitude': tags.get('GPS GPSLatitude', '0'),
        'GPS GPSLongitudeRef': tags.get('GPS GPSLongitudeRef', '0'),
        'GPS GPSLongitude': tags.get('GPS GPSLongitude', '0')
    }
    return info


inf = process_img(test)
print(inf)
