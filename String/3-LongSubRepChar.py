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
# n2
def A(s):
	sub = ""
	ret = 0
	for i in range(len(s)):
		if s[i] in sub:
			j = sub.find(s[i])
			sub = sub[j+1:]
		sub += s[i]
		ret = max(ret,len(sub))
	return ret

# n time using LC SOLN using "sliding window (2 pointers)"
# If using two pointers, use while loop instead of for
def D(s):
	ans = 0
	i,j=0,0
	d={}
	while i < len(s) and j < len(s):
		if s[j] not in d:
			d[s[j]] = s[j]
			j+=1
			ans = max(ans,j-i)
		else:
			del d[s[i]]
			i+=1
	return ans

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "pwwkewwkedw"
s5 = "abcddefghiiijkdlmaop"

s6 = "dvdfg" #edgy1
s7 = "wabcadfgbxyz" #edgy2
s8 = ""

print A(s7)
print D(s7)
