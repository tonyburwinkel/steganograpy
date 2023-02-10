'''
load an image
	get height and width
load a bit list
start a new image with same height and width
loop through bit list and original image pixels
encode all bits in LSBs of pixels
copy remaining bits
save image
'''

from graphics import *
from text_encoder import TextEncoder

se = TextEncoder("hello")
bl = se.steg_final
print(f"num_bits: {''.join(se.num_bits)}")
print(f"steg_final first 16: {''.join(se.steg_final[:16])}")
print(f"steg_final first 16 num: {int(''.join(se.steg_final[:16]),2)}")

pt = Point(0,0)
img = Image(pt, "ppm/maine1.ppm")

wd = img.getWidth()
ht = img.getHeight()
print(f"width {wd} height {ht}")

steg_img = Image(pt, wd, ht)

for i in range(ht*wd):
	# op is a list of 3 ints <=255
	op = img.getPixel(i%wd, i//wd)
	# if we still have bits to encode
	#print(f"op: {i//wd}, {i%ht}")
	if i<len(bl):
		# if the pixel has wrong LSB, change
		if bl[i]=='1' and op[2]%2==0:
			steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2]+1)) 
		else:
			steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2])) 
		if bl[i]=='0' and op[2]%2==1:
			if op[2]<255:
				steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2]+1)) 
			else:
				steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2]-1)) 
		else:
			steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2])) 
	else:
		steg_img.setPixel(i%wd, i//wd, color_rgb(op[0],op[1],op[2]))

steg_img.save("steg_img.ppm")
		
