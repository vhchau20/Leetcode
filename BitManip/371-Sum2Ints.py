# Calculate the sum of two integers a and b, but you are 
# not allowed to use the operator + and -.

# Example 1:
# Input: a = 1, b = 2
# 0000 0001
# 0000 0010
# Output: 3
# 0000 0011

# Example 2:
# Input: a = -2, b = 3
# 1000 0010
# 0000 0011
# Output: 1
# 0000 0001

# 2 = 0000 0010
# 3 = 0000 0011
# 5 = 0000 0101

# Idea is to find the carry so that we can add it 
# WONT WORK FOR NEGATIVE NUMBERS
def A(a,b):
	while b != 0:
		carry = a & b
		a = a ^ b
		b = carry << 1
	return a

def B(a,b):
	# 32 bit mask in hexadecimal
	mask = 0xffffffff
	# works both as while loop and single value check 
	while (b & mask) > 0:
		carry = ( a & b ) << 1
		a = (a ^ b) 
		b = carry
	# handles overflow
	if b > 0:
		return a & mask
	return a


print B(-1,1)