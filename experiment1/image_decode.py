from graphics import *
from image_decoder import ImageDecoder

img = Image((Point(0,0)), "hello.ppm")
imd = ImageDecoder("hello.ppm")

wd = img.getWidth()
ht = img.getHeight()

len_msg = []
msg = []

for i in range(16):
	px = img.getPixel(i,0)
	if px[2]%2:
		len_msg.append('1')
	else:
		len_msg.append('0')

int_length = int(''.join(len_msg),2)

for i in range(16, int_length):
	pn = [i%wd, i//wd]
	px = img.getPixel(i,0)
	if px[2]%2:
		msg.append('1')
	else:
		msg.append('0')

#print(f"message is {len(msg)} bits")
#print(int_length)

print(imd.msg)
