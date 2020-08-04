# Given a singly linked list L: L0-> L1 -> ... -> L_n-1 -> L_n,
# reorder it to: L0 -> Ln -> L1 -> L_n-1 -> L2-> L_n-2 -> ... 

# You may not modify the values in the list's nodes, 
# only nodes itself may be changed.

# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


class node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# 2pass n
# Split LL down the middle
# Reverse the Right Half to get n, n-1, ...
# Merge left and revRight
def A(head):
	# Nothing
	if not head:
		return

	# Get length
	length = 0
	curr = head
	while curr:
		length+=1
		curr = curr.next

	# Get midpoint of list
	midpt = length//2 + length%2

	# Get left and right parts of LL
	left,right=[],[]
	curr = head
	i = 0
	while curr:
		if i < midpt:
			left.append(curr)
		else:
			right.append(curr)
		i+=1
		curr = curr.next 

	# Reverse right part of LL
	revLeft = []
	while left:
		revLeft.append(left.pop())

	# Reorder based on constraint
	ret = []
	while revLeft or right:
		if revLeft:
			ret.append(revLeft.pop())
		if right:
			ret.append(right.pop())

	# Assign next values
	for i in range(1,len(ret)):
		ret[i-1].next = ret[i]
	ret[-1].next = None

	# Return head
	return head

# Creating list of nodes
# a=[node(1),2,3,4] # [1,4,2,3]
a=[node(1),2,3,4,5] # [1,5,2,4,3]
# a=[node(1),2,3,4,5,6] # [1,6,2,5,3,4]

for i in range(1,len(a)):
	a[i] = node(a[i])
	a[i-1].next = a[i]

head = A(a[0])
while head:
	print head.val
	head = head.next