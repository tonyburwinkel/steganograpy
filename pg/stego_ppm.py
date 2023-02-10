from graphics import *
import sys
import math
import text_convert as tc

def main(args):

	#set width and height according to requirements of text (length)
	if len(args)>2:
		print("usage: python3 [stego string]")
		exit(1)
	
	#arg1 should be a string
	
	stego_text = args[1]
	stamp_size = math.ceil(math.sqrt(len(stego_text)*7))

	stego_bits = tc.encode(stego_text)

	width 	= stamp_size
	height 	= stamp_size
	pt = Point(0,0)
	new_img = Image(pt, width, height)

	print("image width: ")
	print(new_img.getWidth())

	#encoding the black pixels with our message:

	for i in range(width):
		for j in range(height):
			new_img.setPixel(i, j, color_rgb(255, 0, 0))

	for i in range(len(stego_bits)):
		if stego_bits[i]=='1':
			new_img.setPixel(i//width, i%height, color_rgb(255, 0, 1))

	new_img.save("steg_stamp.ppm")

if __name__ == "__main__":
	main(sys.argv)
