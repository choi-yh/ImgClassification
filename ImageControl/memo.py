import exifread
import piexif

path = 'C:/Users/HYO/Desktop/sample/20190803_183815.jpg'
f = open(path, 'rb')

read_tag = exifread.process_file(f)
pi_tag = piexif.load(path)
exif_bytes = piexif.dump(pi_tag)

print(read_tag)
print(pi_tag)
print(type(pi_tag))
print(exif_bytes)