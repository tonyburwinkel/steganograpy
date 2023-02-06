from graphics import *
import text_convert as tc

pt = Point(0,0)
name = "steg_stamp.ppm"

img = Image(pt, name)
width = img.getWidth()

px = width**2

bit_list = []
for i in range(px):
		pixel = img.getPixel(i//width,i%width)
		bit_list.append(pixel[2])
		print(f"pixel {i//width},{i%width}'s blue value is {pixel[2]}")

print(bit_list)

ptext = tc.decode(tc.ints_to_chars(bit_list))
print(ptext)
