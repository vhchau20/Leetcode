def getBit(num, i):
	return num & (1 << i)

def setBit(num, i):
	return num | (1 << i)

def clearBit(num, i):
	return num & ~(1 << i)

def updateBit(num, i, j=False):
	value = 1 if j else 0
	mask = ~(1 << i)
	return (num & mask) | (value << i)

# Inverting a num == -(num+1)
def invertNum(num):
	return ~num

def count_one(num):
	count = 0
	while num:
		num = num & (num-1)
		count += 1
	return count

# Set union A | B
# Set intersection A & B
# Set subtraction A & ~B
# Set negation ALL_BITS ^ A or ~A
# Set bit A |= 1 << bit
# Clear bit A &= ~(1 << bit)
# Test bit (A & 1 << bit) != 0
# Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
# Remove last bit A&(A-1)
# Get all 1-bits ~0