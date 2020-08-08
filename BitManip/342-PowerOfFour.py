# Given an integer (signed 32 bits), write a function to 
# check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

# Naive recursion
def A(num):
	if num <= 0:
		return False
	if num % 4:
		return num == 1
	return A(num // 4)

# Naive loop
def B(num):
	if num <= 0:
		return False
	while not num % 4:
		num = num // 4
	return num == 1

# USING BIT MANIP
def C(num):
	if num <= 0:
		return False
	# This removes the LSB ie check if number is power of 2
	if num & (num - 1) != 0:
		return False
	# Power of 2 of even
	if num & 0x55555555 == 0:
		return False
	return True

def D(num):
	print num & (num - 1)
	print num & 0x55555555


print D(1)
print D(4)
print D(5)
print D(16)
print D(19)

