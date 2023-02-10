import unittest
from unittest import TestCase
from text_decoder import TextDecoder
from text_encoder import TextEncoder

'''
this unittest tests the TextDecoder class
'''
class TestDecoder(TestCase):

	def setUp(self):
		self.td = TextDecoder(['1'])

	'''
	make sure method returns properly formatted septets
	'''
	def test_bins_to_septets(self):
		bins=['1','1','0','0','0','0','1']
		self.assertEqual(self.td.bins_to_septets(bins), ["1100001"])
	
	'''
	make sure method returns correct char from binary septet
	'''
	def test_septet_to_char(self):
		septet='1100001'
		self.assertEqual(self.td.septet_to_char(septet), 'a')

	'''
	make sure method take a list of septets and 
	returns the correct string translation
	'''
	def test_septets_to_str(self):
		te = TextEncoder("hello")
		bits = te.bit_list
		seps = self.td.bins_to_septets(bits)
		msg = self.td.septets_to_str(seps)
		self.assertEqual(msg, "hello")
		
if __name__=="__main__":
	unittest.main()
