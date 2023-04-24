from graphics import *

'''
create a fully white image to be lsb encoded

TODO: encode with image_encoder

'''

def main():
	ht = 300
	wd = 300

	white = Image(Point(0,0), wd, ht)

	for i in range(wd):
		for j in range(ht):
			white.setPixel(i, j, "black")

	white.save("black.ppm")



if __name__ == "__main__":
	main()
