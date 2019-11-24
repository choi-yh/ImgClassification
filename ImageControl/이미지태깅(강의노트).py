from PIL import Image # pip install pillow
import piexif # pip install piexif

im = Image.open('C:\\Users\\HYO\\Desktop\\1360546553328.jpg')

if 'exif' not in im.info.keys(): # 이미지파일에 exif 메타정보가 없으면 생성하고
    zeroth_ifd = {piexif.ImageIFD.Make: u"CameraModel",
                  piexif.ImageIFD.XResolution: (0,0),
                  piexif.ImageIFD.YResolution: (0,0),
                  piexif.ImageIFD.Software: u"piexif"
                  }
    exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
                piexif.ExifIFD.LensMake: u"LensMake",
                piexif.ExifIFD.Sharpness: 65535,
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),
                }
    gps_ifd = {piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
               piexif.GPSIFD.GPSAltitudeRef: 1,
               piexif.GPSIFD.GPSDateStamp: u"1999:99:99 99:99:99",
               }
    first_ifd = {piexif.ImageIFD.Make: u"Canon",
                 piexif.ImageIFD.XResolution: (40, 1),
                 piexif.ImageIFD.YResolution: (40, 1),
                 piexif.ImageIFD.Software: u"piexif"
                 }
    exif_dict = {"0th": zeroth_ifd,
                 "Exif": exif_ifd,
                 "GPS": gps_ifd,
                 "1st": first_ifd}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, 'C:\\Users\\HYO\\Desktop\\1360546553328.jpg')

else:  # 메타정보가 있으면 270번 위치에 원하는 텍스트를 부여한 후, 저장한다.
    exif_dict = piexif.load(im.info["exif"])
    exif_dict['0th'][270] = u"drum" # 설명란에 제목, 주제 변경
    exif_bytes = piexif.dump(exif_dict)
    new_file = 'C:\\Users\\HYO\\Desktop\\1360546553328_수정.jpg'
    im.save(new_file, "jpg", exif=exif_bytes)
