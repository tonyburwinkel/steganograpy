from graphics import *
import sys

def get_LSB(val):
	bin_str = str(bin(val))
	return bin_str[len(bin_str)-1]

def main(args):
	name = sys.argv[1]
	# load the image named by sys.argv
	load = Image(Point(0,0), name)
	# get its width and height
	width = load.getWidth()
	height = load.getHeight()
	# move the image centerpoint to where out graphWin's will be
	image = Image(Point(width/2, height/2), name)

	stego_text = []

	for i in range(width):
		for j in range(height):
			pixel = image.getPixel(i, j)
			print(f"pixel {i},{j}'s red value is {bin(pixel[0])}")
			print(f"pixel {i},{j}'s red LSB is {get_LSB(pixel[0])}")
			


	display = GraphWin("myDisplay", width, height)
	image.draw(display)
	display.getMouse()

if __name__ == "__main__":
	main(sys.argv)
