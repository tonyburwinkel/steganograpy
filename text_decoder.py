class TextDecoder:
	def __init__(self, bit_list):
		self.bit_list = bit_list
		self.decoded = self.decode()

	'''
	decode takes a list of bits as strings '1' and '0'
	and converts to a string
	
	params:
		bit_list(list of strings): a list of binary septets as
		'1's and '0's
	returns:
		decoded string that the binary septets encoded
	'''
	def decode(self):
		septets = self.bins_to_septets(self.bit_list)
		return self.septets_to_str(septets)
	
	'''
	decoding helper, changes list of '1's and '0's into 
	list of septets like ['1001000','1101110'...]
	'''
	def bins_to_septets(self, bin_list):
		septets = []
		septet = []
		for i in range(len(bin_list)):
			septet.append(bin_list[i])
			if (len(septet)==7):
				new = ''.join(septet)
				septets.append(new)
				septet = []
	
		return septets
	
	'''
	decode helper
	params: 
		septet (list of '1' and '0'(strings))
	returns:
		char: a single character as a string
	'''
	def septet_to_char(self, septet):
		bin_lit = "0b" + septet
		bin_int = int(bin_lit, 2)
		char = chr(bin_int)
		return char
	
	'''
	decode helper, changes list of binary septet strings 
	to original encoded string (char array)
	
	params:
		septets(list of strings): a list of binary septets as strings
	'''
	def septets_to_str(self, septets):
		chars = []
		for septet in septets:
			new = self.septet_to_char(septet)
			chars.append(new)
		
		return ''.join(chars)
	
