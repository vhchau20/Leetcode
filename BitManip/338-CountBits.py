# Given a non negative integer number num. For every numbers i in the range 
# 0 <= i <= num calculate the number of 1's in their binary representation and 
# return them as an array.

# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]

# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like 
# __builtin_popcount in c++ or in any other language.

# O(n*sizeof(int))
def A(num):
	arr = []
	for i in range(num+1):
		tmp = i
		count = 0
		while tmp:
			tmp = tmp & (tmp-1)
			count += 1
		arr.append(count)
	return arr

# O(n) WIP
def B(num):
	arr = []
	j = 0
	for i in range(num+1):
		j = j | i
		arr.append(j)
	return arr


a=2
b=5
print A(b)
print B(b)