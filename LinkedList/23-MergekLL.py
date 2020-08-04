# Merge k sorted linked lists and return it as 
# one sorted list. Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Should we assume k<n?

class node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# brute force knlogn (apprently fast? beats 92% but bad space, 28%)
def A(lists):
	ret = []
	# kn time
	for i in lists:
		head = i
		while head:
			ret.append(head.val)
			head = head.next
	# nlogn time
	ret.sort()
	if not ret:
		return
	ret[0] = node(ret[0])
	# kntime
	for i in range(1,len(ret)):
		ret[i] = node(ret[i])
		ret[i-1].next = ret[i]
	return ret[0]

import heapq as hq
def B(lists):
	h = []
	for i in lists:
		head = i 
		while head:
			h.append(head.val)
			head = head.next
	hq.heapify(h)
	return h


# TESTING
a=[node(1),4,5]
b=[node(1),3,4]
c=[node(2),6]
for i in range(1,len(a)):
	a[i] = node(a[i])
	a[i-1].next = a[i]
for i in range(1,len(b)):
	b[i] = node(b[i])
	b[i-1].next = b[i]
for i in range(1,len(c)):
	c[i] = node(c[i])
	c[i-1].next = c[i]

head = A([a[0],b[0],c[0]])
while head:
	print head.val
	head = head.next