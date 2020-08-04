# Given two strings s and t , write a function to determine 
# if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? 
# How would you adapt your solution to such case?

def A(s,t):
    Z1 = {}
    Z2 = {}
    for i in s:
        Z1[i] = Z1.get(i,0) + 1
    for i in t:
        Z2[i] = Z2.get(i,0) + 1

    if Z1 == Z2:
        return True

    return False




s1 = "an@gram"
s2 = "nagaram"

print A(s1,s2)
