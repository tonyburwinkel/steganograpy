from graphics import *
from text_encoder import TextEncoder

'''
this class takes a ppm image and hides an ascii message
in the LSBs of the image's pixels

args:
	ptext: (string) plaintext that the user wishes to hide
	image: (string) name of .ppm file to use for stego
'''
class ImageEncoder:
	def __init__(self, ptext, image):
		self.ptext = ptext
		self.te = TextEncoder(ptext)
		# use graphics to load a pixelmap of image
		self.original = Image(Point(0,0), image)
		self.wd = self.original.getWidth()
		self.ht = self.original.getHeight()
		self.steg_image = Image(Point(0,0), self.wd, self.ht)
		self.steg_text = self.te.steg_final

	def encode_pixel(self, old_px, steg_bit):
		if steg_bit=='1'and old_px[2]%2==0:
			return [old_px[0],old_px[1],old_px[2]+1]
		if steg_bit=='0' and old_px[2]%2==1:
			if old_px[2]<255:
				return [old_px[0],old_px[1],old_px[2]+1]
			else:
				return [old_px[0],old_px[1],old_px[2]-1]
		
		return old_px

	def create_steg_img(self):
		pass
