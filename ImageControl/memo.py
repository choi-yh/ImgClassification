import os
import glob

dir = glob.glob('C:\\Users\\HYO\\Desktop\\sample/*.*')
path = os.path.dirname(dir[0])
print(dir)
print(path)