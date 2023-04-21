from graphics import *
import sys

# get an image
original = Image(Point(0,0), sys.argv[1])

wd = original.getWidth()
ht = original.getHeight()

'''
apply an integer from the kernel to an rgb pixel
pixel: a list of 3 integers
number: a single integer
'''
def filter_pixel(pixel, number):
	return [pixel[0]*number, pixel[1]*number, pixel[2]*number]	

'''
take a pixel index and an image
return a 3x3 array containing
the index pixel as position 1, 1
as well as its surrounding 8 neighbors
'''
def get_neighbors(image, i, j):
	cluster = [[None]*3,[None]*3,[None]*3]
	for m in range(-1,2):
		for n in range(-1,2):
			cluster[n+1][m+1] = image.getPixel(i+m, j+n)

	return cluster

'''
apply a 3x3 matrix of integers (kernel)
to a 3x3 matrix of [r,g,b] values (cluster)

returns the value of the new pixel
'''
def apply_kernel(kernel, i, j, image):
	# create a list to hold the new r,g,b values of the filtered pixel
	new_rgb = [0, 0, 0]
	# get the surrounding neighbors of the pixel to be filtered
	# as a cluster of equal dimensions to the kernel
	cluster = get_neighbors(image, i, j)
	filtered = []
	#loop through the kernel and cluster (both are 3x3 arrays)
	for i in range(3):
		for j in range(3):
			# use the filter_pixel helper to apply the kernel's integer
			# to each of the r,g,b values in the cluster at this index
			new_px = filter_pixel(cluster[i][j], kernel[i][j])
			filtered.append(new_px)
	
	for pixel in filtered:
		for k in range(3):
			new_rgb[k] += pixel[k]

	return new_rgb
			
kernel = 	[[-1, -1, -1],
      		[-1, 8, -1],
      		[-1, -1, -1]]
'''

kernel = 	[[0, 1, 0],
      		[1, -4, 1],
      		[0, 1, 0]]
'''

# apply the kernel to each pixel
# save the pixel to a new image in the same position (map it)
# save the resulting image
# show the two next to each other using tk

def create_rs_image(image):
	filtered = Image(Point(0,0), wd, ht)

	for i in range(1, wd-1):
		for j in range(1, ht-1):
			new_px = apply_kernel(kernel, i, j, original)
			print(new_px)
			for k in range(3):
				if new_px[k] < 0:
					new_px[k] = 0
				if new_px[k] > 255:
					new_px[k] = 255
			filtered.setPixel(i, j, color_rgb(new_px[0], new_px[1], new_px[2]))
	
	save_name = f"{sys.argv[1].split('.')[0]}_rs"
	
	filtered.save(f"{save_name}.ppm")

create_rs_image(original)
