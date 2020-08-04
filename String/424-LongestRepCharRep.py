# Given a string s that consists of only uppercase English letters, 
# you can perform at most k operations on that string.

# In one operation, you can choose any character of the string 
# and change it to any other uppercase English character.

# Find the length of the longest sub-string containing all 
# repeating letters you can get after performing the above 
# operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:
# Input:
# s = "ABAB", k = 2
# Output:
# 4
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input:
# s = "AABABBA", k = 1
# Output:
# 4
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, 
# which is 4.

def A(s,k):
	# Get frequency of each letter
	d = {}
	for i in s:
		d[i] = d.get(i,0)+1

	longest = 1
	currLen = 1
	for i in range(1,len(s)):
		if s[i-1] == s[i]:
			currLen += 1
			longest = max(longest,currLen)
		else:
			pass


# A("AABABBA",2)
A("AABABBA",3)