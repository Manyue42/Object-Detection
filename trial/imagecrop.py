import os

os.chdir("G:\Python1\Lib\site-packages\pytesser")
from pytesser import *
from pytesseract import image_to_string
from PIL import Image
from PIL import ImageGrab

# 截图，获取需要识别的区域
x = 345
y = 281
m = 462
n = 327

k = 54
for i in range(2, 6):
    box = (x, y, m, n)
    img = ImageGrab.grab(box)
    img.save("G:\Python1\Lib\site-packages\pytesser\kangkang" + str(i) + ".png")
    # img.show()
    y += 54
    n += 54
