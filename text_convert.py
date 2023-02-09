'''
This module is for converting strings to lists of 1s and 0s
and back again. 
'''

'''
takes a string and converts it into binary septets
returns the septets as a list of strings that are either 1 or 0
'''
def encode(steg_text):
	bit_list=[]
	for i in range(len(steg_text)):
		# convert character to string of 1s and 0s
		bin_str = char_to_bin(steg_text[i])
		for j in range(len(bin_str)):
			bit_list.append(bin_str[j])
	
	return bit_list

'''
helper, changes list of '1's and '0's into list of 1 and 0
'''
def chars_to_ints(bit_list):
	return [int(i) for i in bit_list]

'''
helper, changes list of 1 and 0 to '1' and '0'
'''
def ints_to_chars(int_list):
	return [str(i) for i in int_list]

'''
converts a single character into its binary string literal
'''
def char_to_bin(char):
	bin_lit=(str(bin(ord(char))))
	bin_str=bin_lit[2:]
	if len(bin_str)<7:
		bin_str = '0'+bin_str

	return bin_str

'''
decode takes a list of bits as strings '1' and '0'
and converts to a string

params:
	bit_list(list of strings): a list of binary septets as
	'1's and '0's
returns:
	decoded string that the binary septets encoded
'''
def decode(bit_list):
	septets = bins_to_septets(bit_list)
	return septets_to_str(septets)

'''
decoding helper, changes list of '1's and '0's into 
list of septets like ['1001000','1101110'...]
'''
def bins_to_septets(bin_list):
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
def septet_to_char(septet):
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
def septets_to_str(septets):
	chars = []
	for septet in septets:
		new = septet_to_char(septet)
		chars.append(new)
	
	return ''.join(chars)

