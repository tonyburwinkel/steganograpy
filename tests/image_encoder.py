from graphics import *
from text_encoder import TextEncoder

'''
this class takes a ppm image and hides an ascii message
in the LSBs of the image's pixels

args:
	ptext: (string) plaintext that the user wishes to hide
	image: (string) name of .ppm file to use for stego
		(ImageEncoder will make a copy of this image)
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

	'''
	takes an RGB list and either a '1' or '0'
	and returns an RGB list whose blue value is
	either odd or even, odd if '1', even if '0' recieved
	'''
	def encode_pixel(self, old_px, steg_bit):
		if steg_bit=='1'and old_px[2]%2==0:
			return [old_px[0],old_px[1],old_px[2]+1]
		if steg_bit=='0' and old_px[2]%2==1:
			if old_px[2]<255:
				return [old_px[0],old_px[1],old_px[2]+1]
			else:
				return [old_px[0],old_px[1],old_px[2]-1]
		
		return old_px

	'''
	creates a ppm image with a text string hidden in
	the first i LSBs of the image's pixel map
	'''
	def create_steg_img(self):
		im = self.steg_image
		for i in range(self.ht*self.wd):
			# generate pixel index based on i
			pn = [i%self.wd, i//self.wd]
			# get the original image's pixel at this index
			op = self.original.getPixel(pn[0],pn[1])
			# if we still have bits to encode
			if i<len(self.steg_text):
				# create an RGB value given the original pixel
				np = self.encode_pixel(op, self.steg_text[i])
				# set the new image's pixel to this RGB
				im.setPixel(pn[0],pn[1], color_rgb(np[0],np[1],np[2]))
			# if we are done encoding stego bits
			else:
				# set the remaining pixels to the original's values
				im.setPixel(pn[0],pn[1], color_rgb(op[0],op[1],op[2]))

	'''
	saves the created stego image under [name]
	'''
	def save_steg_image(self, name):
		self.steg_image.save(name)
