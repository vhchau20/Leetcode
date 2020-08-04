# Given a linked list, remove the n-th node from the end of list 
# and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list 
# becomes 1->2->3->5.

# Note:
# Given n will always be valid.

# Follow up:
# Could you do this in one pass?


class node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# 2pass n
def A(head,n):
	# Empty LL
	if not head:
		return 

	# Get length
	length = 0
	curr = head
	while curr:
		length+=1
		curr = curr.next

	# Get node to remove
	nodeToRem = length-n

	# Check if node to remove is first node
	if nodeToRem <= 0:
		return head.next

	# Restart fields
	curr = head
	prev = None
	i = 0

	# Loop through LL and remove node while updating fields
	while curr:
		# Know which node we should move to next
		tmp = curr.next

		# Check if current node is the one to remove
		if i == nodeToRem:
			curr = curr.next
			prev.next = curr

		# Update prev
		prev = curr

		# Update curr node
		curr = tmp
		i+=1

	return head

# 2pass n using dummy node
def B(head,n):
	# Use dummy to make it easy to return
	dummy = node(0)
	dummy.next = head

	length = 0
	curr = head
	while curr:
		length+=1
		curr = curr.next

	nodeToRem = length - n
	curr = dummy
	while nodeToRem > 0:
		nodeToRem -= 1
		curr = curr.next

	curr.next = curr.next.next
	return dummy.next


# TESTING
a=[node(1),2,3,4,5]
for i in range(1,len(a)):
	a[i] = node(a[i])
	a[i-1].next = a[i]

head = B(a[0],2)
while head:
	print head.val
	head = head.next