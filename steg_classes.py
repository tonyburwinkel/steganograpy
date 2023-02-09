import text_convert as tc

'''
this class is for taking a plaintext
and encoding a stego bit list

the first 16 elements in the bit list
should be a left 0 padded binary number
representing the total number of bits encoded
(including this number)
'''
class StegoEncoder:
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
		# create binary literal and remove 0b from front
		bin_num_lit = (bin(len(self.bit_list)))[2:]
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
				bit_list.append(bin_str[j])
	
		return bit_list

	'''
	encode helper, takes a char and converts to 
	a binary string with 7 bits
	'''
	def char_to_bin(self, char):
		bin_lit=(str(bin(ord(char))))
		bin_str=bin_lit[2:]
		if len(bin_str)<7:
			bin_str = '0'+bin_str

		return bin_str

	def make_steg_final(self):
		final = []
		for i in range(len(self.num_bits)):
			final.append(self.num_bits[i])
		for i in range(len(self.bit_list)):
			final.append(self.bit_list[i])
		return final

st = StegoEncoder("hi")
print(len(st.steg_final))
