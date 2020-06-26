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

def algo(l1,l2):
	if not l1 and not l2:
		return []
	if not l1:
		return l2
	if not l2:
		return l1
	l = l1
	r = l2
	s = []
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
	# Append the reest of r
	while r != None:
		s.append(r)
		r = r.next

	for i in range(1,len(s)):
		first = s[i-1]
		second = s[i]
		first.next = second

	return s[0]

A=[1,3,5,7,9]
# A=[1,3,5]
j = node(A[0])
s = [j]
for i in range(1,len(A)):
	k = node(A[i])
	s[i-1].next = k
	s.append(k)

B=[2,4,6,8,10]
# B=[1,1,4]
m = node(B[0])
u = [m]
for i in range(1,len(B)):
	k = node(B[i])
	u[i-1].next = k
	u.append(k)

ret = algo(j,m)
while ret:	
	print ret.val
	ret = ret.next