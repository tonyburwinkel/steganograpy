Simple steganography tool written in Python

This program is for hiding messages in images. 

The provided tools take a message written in ascii text and encode the message
into the least significant bits of the image's pixels (specifically the blue values in RGB).

TODO:

implement image encoder with PIL instead of Zelle's 
implement bitwise steganalysis of bit planes with bitmasking
