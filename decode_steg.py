from graphics import *
import text_convert as tc

def main(args):

				pt = Point(0,0)
				name = args[1]

				img = Image(pt, name)
				width = img.getWidth()
				height = img.getHeight()

				px = width*height

				bit_list = []
				for i in range(px):
						pixel = img.getPixel(i//width,i%height)
						bit_list.append(pixel[2]%2)
				
				ptext = tc.decode(tc.ints_to_chars(bit_list))
				print(ptext[:100])


if __name__ == "__main__":
	main(sys.argv)
