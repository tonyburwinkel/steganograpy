import unittest
from unittest import TestCase
from rs_kernel import filter_pixel, get_neighbors, apply_kernel

'''
this unittest tests the TextDecoder class
'''
class TestDecoder(TestCase):

	'''
	make sure method returns properly formatted septets
	'''
	def test_filter_pixel(self):
		pixel = [25, 25, 25]
		new_px = filter_pixel(pixel, 2)
		self.assertEqual(new_px, [50,50,50])

	'''
	make sure method returns properly formatted septets
	'''
	def test_get_neighbors(self):
		pixel = [25, 25, 25]
		new_px = filter_pixel(pixel, 2)
		self.assertEqual(new_px, [50,50,50])

if __name__=="__main__":
	unittest.main()
