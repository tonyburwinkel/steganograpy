from graphics import *
# from text_encoder import TextEncoder
from image_encoder import ImageEncoder

ie = ImageEncoder("hello","ppm/maine1.ppm")

op = [0,0,1]

ie.create_steg_img()
ie.save_steg_image("hello.ppm")
