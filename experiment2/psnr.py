import sys
from PIL import Image

def psnr(img1_path, img2_path):
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
    mse /= (img1.width * img1.height)

    # Calculate the peak signal-to-noise ratio (PSNR)
    psnr = 10 * (3 * img1.width * img1.height)**0.5 / mse**0.5

    return psnr

# Get the file paths from command line arguments
if len(sys.argv) < 3:
    print("Usage: python psnr.py <img1_path> <img2_path>")
    sys.exit(1)
img1_path = sys.argv[1]
img2_path = sys.argv[2]

# Calculate the PSNR and print the result
psnr_value = psnr(img1_path, img2_path)
print("PSNR:", psnr_value, "dB")
