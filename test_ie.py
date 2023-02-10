import unittest
from unittest import TestCase
from text_encoder import TextEncoder
from image_encoder import ImageEncoder

'''
this unittest tests the StegoEncoder class
'''
class TestImageEncoder(TestCase):

	def setUp(self):
		self.ie = ImageEncoder("hello", "ppm/maine1.ppm")

	'''
	make sure bit value '1' applied to odd
	blue valued pixel returns a pixel RGB list
	with an odd blue value
	'''
	def test_encode_1_pixel_odd(self):
		px = self.ie.encode_pixel([0,0,1], '1')
		self.assertEqual(px, [0,0,1])

	'''
	make sure bit value '1' applied to even
	blue valued pixel returns a pixel RGB list
	with an odd blue value
	'''
	def test_encode_1_pixel_even(self):
		px = self.ie.encode_pixel([0,0,0], '1')
		self.assertEqual(px, [0,0,1])

	'''
	make sure bit value '0' applied to odd
	blue valued pixel returns a pixel RGB list
	with an even blue value 
	'''
	def test_encode_0_pixel_odd(self):
		px = self.ie.encode_pixel([0,0,1], '0')
		self.assertEqual(px, [0,0,2])

	'''
	make sure bit value '0' applied to even
	blue valued pixel returns a pixel RGB list
	with an even blue value
	'''
	def test_encode_0_pixel_even(self):
		px = self.ie.encode_pixel([0,0,0], '0')
		self.assertEqual(px, [0,0,0])

	'''
	make sure bit value '0' applied to odd
	blue valued pixel > 254 returns a pixel RGB list
	with an even blue value < 255
	'''
	def test_encode_0_pixel_odd_255(self):
		px = self.ie.encode_pixel([0,0,255], '0')
		self.assertEqual(px, [0,0,254])


if __name__=="__main__":
	unittest.main()
