# Given a string, find the length of the longest substring without 
# repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a 
# subsequence and not a substring.

import collections as c
# O(n)
def A(s):
	sub = ""
	ret = 0
	for i in range(len(s)):
		if s[i] in sub:
			j = sub.find(s[i])
			sub = sub[j+1:]
		sub += s[i]
		if len(sub) > ret:
			ret = len(sub)
	return ret

# O(n) use enumerate()?
def B(s):
	pass

str1 = "abcabcbb"
str2 = "bbbbb"
str3 = "pwwkew"
str4 = "pwwkewwkedw"
str5 = "abcddefghiiijkdlmaop"
str6 = "dvdf"

print(A(str5))