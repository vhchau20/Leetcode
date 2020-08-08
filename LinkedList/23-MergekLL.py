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


from LINK import makeLL, printLL
a=[1,4,5]
b=[1,3,4]
c=[2,6]
headA=makeLL(a)
headB=makeLL(b)
headC=makeLL(c)

printLL(A([headA,headB,headC]))
