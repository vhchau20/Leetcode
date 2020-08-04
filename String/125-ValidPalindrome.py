# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define 
# empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false


# Know how to use join()
def A(s):
	s = "".join((char if char.isalpha() or char.isdigit() else "") for char in s).lower()
	for i in range(len(s) // 2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

a = "A man, a plan, a canal: Panama"
b = "race a car"

print A(a)
