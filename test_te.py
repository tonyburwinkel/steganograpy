import unittest
from unittest import TestCase
from text_encoder import TextEncoder

'''
this unittest tests the StegoEncoder class
'''
class TestEncoder(TestCase):

	'''
	make sure ptext is stored and unaltered
	'''
	def test_ptext_stored(self):
		te = TextEncoder("howdy pard")
		self.assertEqual(te.ptext, "howdy pard")

	'''
	make sure bit list is correct length
	'''
	def test_bit_list_length(self):
		te = TextEncoder("hi")
		self.assertEqual(len(te.bit_list),14)

	'''
	make sure bit list is correct sequence
	'''
	def test_bit_list_contents(self):
		te = TextEncoder("hi")
		exp_bits = ['1','1','0','1','0','0','0',
			'1','1','0','1','0','0','1']
		self.assertEqual(te.bit_list,exp_bits)

	'''
	make sure num bits is always padded to 16
	'''
	def test_len_num_bits(self):
		te = TextEncoder("hi")
		self.assertEqual(len(te.num_bits),16)

	'''
	make sure num bits is correct number
	'''
	def test_num_bits_correct(self):
		te = TextEncoder("hi")
		lit = ''.join(te.num_bits)
		self.assertEqual(int(lit,2), 30)
		te = TextEncoder("hello")
		lit = ''.join(te.num_bits)
		self.assertEqual(int(lit,2), 51)

	'''
	make sure steg_final list is the right length
	'''
	def test_steg_final_length(self):
		te = TextEncoder("hi")
		self.assertEqual(len(te.steg_final),30)
		te = TextEncoder("hello world")
		self.assertEqual(len(te.steg_final),93)

if __name__=="__main__":
	unittest.main()
