from graphics import *
import sys


# Open the image file
filename = sys.argv[1]
savename = sys.argv[2]
img = Image(Point(0, 0), filename)

# Get the dimensions of the image
width = img.getWidth()
height = img.getHeight()

# Create a new image object to store the grayscale version
gray_img = Image(Point(0, 0), width, height)

# Loop through every pixel in the original image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the current pixel
        r, g, b = img.getPixel(x, y)

        # Calculate the grayscale value
        gray_val = int(0.299 * r + 0.587 * g + 0.114 * b)

        # Set the RGB values of the corresponding pixel in the grayscale image
        gray_img.setPixel(x, y, color_rgb(gray_val, gray_val, gray_val))

# Save the grayscale image to a file
gray_img.save(f"{savename}.ppm")
