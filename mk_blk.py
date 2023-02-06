from graphics import *
import sys

'''
script creates a ppm image from a provided width and height,
sets all pixels to black, and saves the image
'''
def main(args):

	width = int(args[1])
	height = int(args[2])
	pt = Point(0,0)
	new_img = Image(pt, width, height)

	for i in range(width):
		for j in range(height):
			new_img.setPixel(i, j, color_rgb(0, 0, 0))

	new_img.save(args[3])

if __name__ == "__main__":
	main(sys.argv)
