# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the
# first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def A(l1,l2):
	if not l1 and not l2:
		return []
	if not l1:
		return l2
	if not l2:
		return l1
	l = l1
	r = l2
	s = []
	# Iterate through each LL until we reach length of 
	# shorter LL
	while l != None and r != None:
		if l.val == r.val:
			s.append(l)
			s.append(r)
			l = l.next
			r = r.next
		elif l.val < r.val:
			s.append(l)
			l = l.next
		elif l.val > r.val:
			s.append(r)
			r = r.next
	# Append the rest of l
	while l != None:
		s.append(l)
		l = l.next
	# Append the rest of r
	while r != None:
		s.append(r)
		r = r.next

	for i in range(1,len(s)):
		first = s[i-1]
		second = s[i]
		first.next = second

	return s[0]


# TESTING
a=[node(1),3,5,7,9]
for i in range(1,len(a)):
	a[i] = node(a[i])
	a[i-1].next = a[i]

b=[node(2),4,6,8,10]
for i in range(1,len(b)):
	b[i] = node(b[i])
	b[i-1].next = b[i]

head = A(a[0],b[0])
while head:	
	print head.val
	head = head.next