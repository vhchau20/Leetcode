# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either 
# iteratively or recursively. Could you implement both?

class node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# O(n) using stack
def algo(head):
	if head == None:
		return 
	if head.next == None:
		return head

	s, curr = [], head
	while curr.next != None:
		s.append(curr)
		curr = curr.next
	s.append(curr)

	head = s[-1]

	while s:
		if len(s) == 1:
			j = s.pop()
			j.next = None
			break
		i = s.pop()
		i.next = s[-1]

	return head

# O(n) using recursion
def algo2(head):
	pass
	if head == None:
		return 
	if head.next == None:
		return head




A=node(1)
B=node(2)
C=node(3)
D=node(4)
E=node(5)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = None

print algo(A).val