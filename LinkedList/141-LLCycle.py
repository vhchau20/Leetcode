# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, 
# we use an integer pos which represents the position (0-indexed) 
# in the linked list where tail connects to. If pos is -1, 
# then there is no cycle in the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# 3->2->0->-4
#    2<-<-<-v
# Output: true
# Explanation: There is a cycle in 
# the linked list, where tail connects to the second node.


# n time using map
# Use map to check if visited
# n space
def A(head):
	d = {}
	curr = head
	while curr:
		if curr.next in d:
			return True
		else:
			d[curr] = True
		curr = curr.next
	return False

# LC SOLN
# Using slow and fast pointers to check for cycle
# n time but O(1) space
def B(head):
	if not head or not head.next:
		return False
	slow = head
	fast = head.next
	while slow != fast:
		if not fast or not fast.next:
			return False
		slow = slow.next
		fast = fast.next.next
	return True


from LINK import makeLL,printLL,getTail
a=[3,2,0,-4]
head=makeLL(a)
tail=getTail(head)

# Make cycle between -4 -> 2
tail.next = head.next

print B(head)
