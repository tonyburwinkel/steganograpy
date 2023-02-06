
'''
This module is for converting strings to lists of 1s and 0s
and back again. 
'''

steg_text = "cat"

'''
takes a string and converts it into binary septets
returns the septets as a list strings that are either 1 or 0
'''
def make_steg(steg_text):
	bit_list=[]
	for i in range(len(steg_text)):
		# convert character to string of 1s and 0s
		bin_str = char_to_bin(steg_text[i])
		for j in range(2, len(bin_str)):
			bit_list.append(bin_str[j])

	return bit_list

def chars_to_ints(bit_list):
	return [int(i) for i in bit_list]

def ints_to_chars(int_list):
	return [str(i) for i in int_list]

def char_to_bin(char):
	return str(bin(ord(char)))

#convert a list of 1s and 0s to binary septets
# add 7 characters to list
# join list and add joined to return list
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

def septet_to_char(septet):
	bin_lit = "0b" + septet
	bin_int = int(bin_lit, 2)
	char = chr(bin_int)
	print("char: " + char)
	return char

def septets_to_str(septets):
	chars = []
	for septet in septets:
		new = septet_to_char(septet)
		chars.append(new)
	
	return ''.join(chars)

def decode(bit_list):
	septets = bins_to_septets(bit_list)
	return septets_to_str(septets)
	
	
