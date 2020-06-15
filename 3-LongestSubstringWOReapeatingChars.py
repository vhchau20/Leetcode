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
# O(n^2)
def A(s):
	sub = ""
	solns = []
	for i in range(len(s)):
		if s[i] in sub:
			j = sub.find(s[i])
			sub = sub[j+1:]
		sub += s[i]
		solns.append(sub)
	ret = 0
	for i in solns:
		if len(i) > ret:
			ret = len(i)
	print(solns)
	return ret

# O(n)
def B(s):
    longest = 0
    seen_more = 0
    chars = {}

    for i, c in enumerate(s):
    	print((i,c))
        if c not in chars or chars[c] < seen_more:
                longest = max(longest, i - seen_more + 1)
        else:
            seen_more = chars[c] + 1
        chars[c] = i
    return longest

def C(s):
	sol = 0

str1 = "abcabcbb"
str2 = "bbbbb"
str3 = "pwwkew"
str4 = "pwwkewwkedw"
str5 = "abcddefghiiijkdlmaop"
str6 = "dvdf"

# print(A(str6))
print(B(str6))





