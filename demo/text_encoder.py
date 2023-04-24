'''
this class is for taking a plaintext
and encoding a stego bit list

attributes:
	ptext: original plaintext, passed as only arg to constructor
	bit_list: ptext encoded as list of '1's and '0's (strings)
		for easy concatenation
	num_bits: number of bits in bit_list plus 16 (length of num_bits)
		expressed as a binary number of 16 bits
	steg_final: message ready to encode into image LSBs
		1st 16 elements are total length of list
		remaining elements are the encoded message

the first 16 elements in the bit list
should be a left 0 padded binary number
representing the total number of bits encoded
(including this number)
'''
class TextEncoder:
	def __init__(self, ptext):
		self.ptext = ptext
		self.bit_list = self.encode_text(ptext)
		self.num_bits = self.encode_bit_length()
		self.steg_final = self.make_steg_final()
		
	'''
	takes the number of bits to be encoded
	and returns a left padded 16 bit binary
	number conversion of the number
	'''
	def encode_bit_length(self):
		# count number of bits in encoded list + number 
		# of bits used to encode length (16)
		total_bits = len(self.bit_list) + 16
		# create binary literal and remove 0b from front
		bin_num_lit = (bin(total_bits))[2:]
		lit_list = [bin_num_lit[i] for i in range(len(bin_num_lit))]
		while(len(lit_list)<16):
			lit_list.insert(0,'0')

		return lit_list

	'''
	takes a string and converts it into binary septets
	returns the septets as a list of strings that are either 1 or 0
	'''
	def encode_text(self, ptext):
		bit_list=[]
		for i in range(len(ptext)):
			# convert character to string of 1s and 0s
			bin_str = self.char_to_bin(ptext[i])
			for j in range(len(bin_str)):
			# add all of these bits to a list 
				bit_list.append(bin_str[j])
	
		return bit_list

	'''
	encode helper, takes a char and converts to 
	a binary string with 7 bits
	create a binary literal from a char -> a = '1100001'
	'''
	def char_to_bin(self, char):
		bin_lit=(str(bin(ord(char)))) 
		bin_str=bin_lit[2:]
		while len(bin_str)<7:
			bin_str = '0'+bin_str

		return bin_str

	'''
	creates a stego text from the 0 padded message length
	added to the plaintext encoded as septets

	returns a list whose 1st 16 chars are the encoded message length
	(in bits) and whose remainder is the message encoded as septets
	'''
	def make_steg_final(self):
		final = []
		for i in range(len(self.num_bits)):
			final.append(self.num_bits[i])
		for i in range(len(self.bit_list)):
			final.append(self.bit_list[i])
		return final

