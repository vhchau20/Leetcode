# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# O(n2)
def A(nums, target):
	pass
	for i in range(len(nums)):
		j = target - nums[i]
		for k in range(i,len(nums)):
			if nums[k] == j:
				return [nums[i],nums[k]]
	return

def B(nums, target):
	d = {}
	for i in nums:
		d[i] = target-i
	for i in range(len(nums)):
		if d[nums[i]] in d:
			return [i, d[nums[i]]]

a = [2, 7, 11, 15, 9, 10]
print B(a,18)

May 2018 - Present
Front-End Engineer