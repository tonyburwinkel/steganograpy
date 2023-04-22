from graphics import *

'''
take each pixel in an image
take each RGB of the pixel
	if the RGB is odd, turn the value all the way up
	if the RGB is even, turn the value off

should create an image with a 6 color palette
should also reveal LSB stego in areas of high saturation

goal: display both images on screen
'''

def lsb_expose(name):
	original = Image(Point(0,0), name)
	ht = original.getHeight()
	wd = original.getWidth()

	lsb = Image(Point(0,0), wd, ht)

	for i in range(wd):
		for j in range(ht):
			px = original.getPixel(i, j)
			new_px = [0]*3
			for k in range(3):
				if px[k]%2==1:
					new_px[k]=255
			lsb.setPixel(i, j, color_rgb(new_px[0],new_px[1],new_px[2]))

	lsb.save(f"{name.split('.')[0]}_lsb.ppm")

