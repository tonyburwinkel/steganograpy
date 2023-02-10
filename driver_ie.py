from graphics import *
# from text_encoder import TextEncoder
from image_encoder import ImageEncoder

ie = ImageEncoder("hello","ppm/maine1.ppm")

op = [0,0,1]

print(ie.encode_pixel(op,'0'))
print(op[2]%2)
