import glob
import cv2
import exifread
import random

dir_path = glob.glob('C:/Users/HYO/Desktop/sample/*.jpg')
test = random.choice(dir_path)


# (16, 16) 사이즈 binary image 변환
def img2hash(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (16, 16))
    avg = img.mean()  # 픽셀 평균값 구하기
    bi = 1 * (img > avg)  # 픽셀 평균값보다 큰 픽셀 갯수 구하기
    return bi


def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a != b).sum()
    return distance


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


# 유사 이미지 찾기
def findImg(file_path, query):
    # 대상 이미지 불러오기
    query_img = cv2.imread(query, cv2.IMREAD_COLOR)
    query_img = cv2.resize(query_img, (400, 400))
    query_hash = img2hash(query_img)
    query_inf = process_img(query) # 태그 정보 붙여줄 대상

    cv2.imshow('query', query_img) # 대상 이미지 띄워놓기

    for path in file_path:
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (400, 400))

        cv2.imshow("Searching...", img)
        cv2.waitKey(5)

        # hamming distance 를 통해 비교하기
        img_hash = img2hash(img)
        dst = hamming_distance(query_hash, img_hash) / 256
        if dst < 0.20: # hamming distance 가 75퍼 이상 유사하면 출력
            tags = process_img(path)
            # gps 정보가 없을 때 태그 입력해주기


            print(path, dst, tags)
            cv2.imshow(path, img)
    cv2.destroyWindow("Searching...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


test = random.choice(dir_path)
findImg(dir_path, test)
