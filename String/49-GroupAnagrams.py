# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


# n3 naive
def A(strs):
	B = {}
	for i in strs:
		j = "".join(sorted(i))
		B[j] = B.get(j,0) + 1

	ret = []

	for i in B:
		C = []
		for j in strs:
			k = "".join(sorted(j))
			if i == k:
				C.append(j)
		ret.append(C)
	
	return ret

def B(strs):
	pass






s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print A(s)
