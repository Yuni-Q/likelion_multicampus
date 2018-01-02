# PIL, OpenCV
# python3 : pillow
# pip install Pillow
# https://pillow.readthedocs.io/en/4.3.x/
from PIL import Image, ImageFilter, ImageDraw,ImageFont

im = Image.open("aa.jpg")
print ("image info : " + str(im.info))

print ("image size : " + str(im.size))

print ("image format : " + str(im.format))

#print (im.getpixel('1','1')

lrim = im.transpose(Image,FLIP_LEFT_RIGHT)
lrim = save('a_lr.jpg')
# 좌우 반전
lrim = im.transpose(Image,FLIP_TOP_BOTTOM)
lrim = save('a.tb.jpg')
# 상하 반전
size = (64,64)
img2 = im.thumnail(size)
img2.save('a_thum.jpg')
# 썸네일 만들기
img3 = im.rotate(90)
img3.save('a_90,jpg')
# 90도 회전

img4 = im.resize(1000,1000)
img4.svae('a_1000.jpg')
#크기조절
cropImg = im.crop(100,100,150,150)
cropImg.svae('a_crop.jpg')
#크기조절
blurImg = im.filter(ImageFilter.SHARPEN)
blurImg.save('a_blur.jpg')
#필터

font_size =36
width = 500
height = 1 100
back_ground_color = (255,255,255)

font_color= (0,0,0)
unicode_text = 'python is good'

im = Image.new('RGB', (width, height), back_ground_color )
draw = ImageDraw.Draw(im)
draw.text((10,10),unicode_text,fill=font_color)

im.save("text.jpg")