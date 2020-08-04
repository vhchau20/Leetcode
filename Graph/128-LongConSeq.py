# Given an unsorted array of integers, 
# find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) 
# complexity.

# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive 
# elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def A(nums):
	nums = set(nums)
	best = 0
	for x in nums:
		if x - 1 not in nums:
			y = x + 1
			while y in nums:
				y += 1
			best = max(best, y - x)
	return best


print A([100,4,200,1,3,2])