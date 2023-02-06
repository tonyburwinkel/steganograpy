bin_num = (bin(ord("!")))

print(bin_num)
str_num = str(bin_num)

for i in range(len(str_num)):
	print(f"{str_num[i]} i")

# last digit in binary string
print(str_num[len(str_num)-1])

print(chr(0b1000001))

print(f"255 in binary is {bin(255)}")

