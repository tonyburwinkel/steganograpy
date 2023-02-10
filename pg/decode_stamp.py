from graphics import *
import text_convert as tc

def main(args):

				pt = Point(0,0)
				name = args[1]

				img = Image(pt, name)
				width = img.getWidth()

				px = width**2

				bit_list = []
				for i in range(px):
						pixel = img.getPixel(i//width,i%width)
						bit_list.append(pixel[2])

				ptext = tc.decode(tc.ints_to_chars(bit_list))
				print(ptext)


if __name__ == "__main__":
	main(sys.argv)
