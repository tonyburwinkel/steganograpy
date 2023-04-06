from graphics import *

'''
create a fully white image to be lsb encoded

TODO: encode with image_encoder

'''

def main():
	ht = 400
	wd = 400

	white = Image(Point(0,0), wd, ht)

	for i in range(wd):
		for j in range(ht):
			white.setPixel(i, j, "white")

	white.save("white.ppm")



if __name__ == "__main__":
	main()
