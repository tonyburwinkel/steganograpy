from image_encoder import ImageEncoder

gravity = ''

with open("gravity.txt", "r") as f:
	for line in f:
		gravity+=line

print(gravity)

ie = ImageEncoder(gravity, "white.ppm")
ie.create_steg_img()
ie.save_steg_image("gravity.ppm")
