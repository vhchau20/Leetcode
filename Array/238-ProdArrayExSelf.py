# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal 
# to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements 
# of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? 
# (The output array does not count as extra space for the purpose of space complexity analysis.)


# naive n2
def A(nums):
	n = len(nums)
	output = [1]*n

	for i in range(n):
		for j in range(n):
			if i != j:
				output[j] *= nums[i]

	return output

# n but using division
def B(nums):
	output = []

	totalProd = 1
	for i in nums:
		totalProd *= i

	for i in nums:
		output.append(totalProd/i)

	return output

# Idea is to use 2 pointers at each end of nums,
# update pointers after each iterations with nums[i,-i-1]
def C(nums):
	n = len(nums)
	output = [1]*n

	left = 1
	right = 1
	
	for i in range(n):
		output[i] *= left
		output[-1-i] *= right
		left *= nums[i]
		right *= nums[-1-i]

	return output

def D(nums):
	n = len(nums)
	output = []

	# traverse forwards
	p = 1
	for i in range(n):
		output.append(p)
		print output
		p *= nums[i]
	
	# traverse backwards
	p = 1
	for i in range(n-1,-1,-1):
		output[i] *= p
		p *= nums[i]

	return output







a=[1,2,3,4]
print D(a)