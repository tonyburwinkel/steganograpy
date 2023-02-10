from graphics import *

img = Image((Point(0,0)), "steg_img.ppm")

len_msg = []

for i in range(16):
	px = img.getPixel(i,0)
	print(f"{px} becomes {px[2]%2}")
	if px[2]%2:
		len_msg.append('1')
	else:
		len_msg.append('0')

print(''.join(len_msg))
print(int(''.join(len_msg),2))


