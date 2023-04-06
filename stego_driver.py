from graphics import *
# from text_encoder import TextEncoder
from image_encoder import ImageEncoder


def main():
	if len(sys.argv)<3:
		print("usage: python3 stego_driver.py [cover_image] [save_name] [stego_text.txt]")

	stego_string = "meet me at mignight by the old oak tree"
	
	ie = ImageEncoder(stego_string, sys.argv[1])
	
	ie.create_steg_img()
	ie.save_steg_image(f"{sys.argv[2]}.ppm")

if __name__ == "__main__":
	main()
