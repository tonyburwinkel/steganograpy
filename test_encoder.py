import unittest
from unittest import TestCase
from encoder import StegoEncoder

'''
this unittest tests the StegoEncoder class
'''
class TestEncoder(TestCase):

	'''
	make sure ptext is stored and unaltered
	'''
	def test_ptext_stored(self):
		se = StegoEncoder("howdy pard")
		self.assertEqual(se.ptext, "howdy pard")

	'''
	make sure bit list is correct length
	'''
	def test_bit_list_length(self):
		se = StegoEncoder("hi")
		self.assertEqual(len(se.bit_list),14)

	'''
	make sure bit list is correct sequence
	'''
	def test_bit_list_contents(self):
		se = StegoEncoder("hi")
		exp_bits = ['1','1','0','1','0','0','0',
			'1','1','0','1','0','0','1']
		self.assertEqual(se.bit_list,exp_bits)

	'''
	make sure num bits is always padded to 16
	'''
	def test_len_num_bits(self):
		se=StegoEncoder("hi")
		self.assertEqual(len(se.num_bits),16)

	'''
	make sure num bits is correct number
	'''
	def test_num_bits_correct(self):
		se=StegoEncoder("hi")
		lit = ''.join(se.num_bits)
		self.assertEqual(int(lit,2), 30)
		se=StegoEncoder("hello")
		lit = ''.join(se.num_bits)
		self.assertEqual(int(lit,2), 51)

	'''
	make sure steg_final list is the right length
	'''
	def test_steg_final_length(self):
		se=StegoEncoder("hi")
		self.assertEqual(len(se.steg_final),30)
		se=StegoEncoder("hello world")
		self.assertEqual(len(se.steg_final),93)

if __name__=="__main__":
	unittest.main()
