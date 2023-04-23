import sys
import math
from PIL import Image

def get_psnr(img1_path, img2_path):
# Open the images and convert to RGB mode
	img1 = Image.open(img1_path).convert('RGB')
	img2 = Image.open(img2_path).convert('RGB')

# Calculate the mean squared error (MSE) between the images
	mse = 0
	for i in range(img1.width):
		for j in range(img1.height):
			r1, g1, b1 = img1.getpixel((i,j))
			r2, g2, b2 = img2.getpixel((i,j))
			mse += (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
	mse /= 3*(img1.width * img1.height)

# Calculate the peak signal-to-noise ratio (PSNR)
	print(mse)
	if mse == 0:
		return 0

	print(math.log(255/mse, 10))
	#psnr = 10 * (3 * img1.width * img1.height)**0.5 / mse**0.5
	psnr = 10 * math.log10(255**2/mse)

	return psnr
