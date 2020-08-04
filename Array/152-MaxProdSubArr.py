# Given an integer array nums, find the contiguous subarray 
# within an array (containing at least one number) 
# which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] 
# is not a subarray.


# naive n!
def A(nums):
	n = len(nums)
	maxProd = nums[0]

	for i in range(n):
		for j in range(i+1,n+1):
			sub = nums[i:j]
			prod = 1
			for k in sub:
				prod *= k
			if prod > maxProd:
				maxProd = prod

	return maxProd

def B(nums):
	n = len(nums)
	maxProd = max(nums)
	totalProd = 1
	for i in range(n):
		pass

	for i in range(n):
		# Get left subarray
		leftSub = nums[:-i-1]
		# Get right subarray
		rightSub = nums[i+1:]

		for i in leftSub:
			leftProd *= i
		for i in rightSub:
			rightProd *= i

		if leftProd > maxProd:
			maxProd = leftProd
		if rightProd > maxProd:
			maxProd = rightProd

	return maxProd


a = [-3,-1,2,3,4,-2,6,-2,-3]
c = [2,3,-2,4]
b = [-2,0,-1]
d = [2,-2,-2]

print A(a)