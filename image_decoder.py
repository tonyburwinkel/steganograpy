from graphics import *
from text_decoder import TextDecoder

'''
this class decodes the message hidden in the LSBs
of a steg_image created with ImageEncoder class
'''
class ImageDecoder:
	def __init__(self, fname):
		self.steg_img = Image(Point(0,0), fname)
		self.wd = self.steg_img.getWidth()
		self.ht = self.steg_img.getHeight()
		self.msg_len = self.get_msg_len
		self.msg_bits = self.get_msg_bits
		self.td = TextDecoder(self.msg_bits)
		self.msg = td.decoded()

	def get_msg_len(self):
		length = []
		for i in range(16):
			px = steg_img.getPixel(i,0)
			if px[2]%2:
				length.append('1')
			else:
				length.append('0')

		return int(''.join(length), 2)

	def get_msg_bits(self):
		msg_bits = []
		for i in range(16, self.msg_len):
			pn = [i%self.wd, i//self.wd]
			px = self.steg_img.getPixel(pn[0],pn[1])
			if px[2]%2:
				msg.append('1')
			else:
				msg.append('0')

		return msg_bits
