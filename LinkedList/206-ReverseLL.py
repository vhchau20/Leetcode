# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either 
# iteratively or recursively. Could you implement both?

# 2pass n using stack
def A(head):
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

# n via recursion WIP
def B(head):
	head = B_helper(head,None)
	return head

def B_helper(node,prev):
	if node == None:
		return prev
	tmp = node
	nextN = node.next
	node.next = prev
	return B_helper(nextN, tmp)

# n using prev variable
def C(head):
	prev = None
	curr = head
	while curr:
		tmp = curr.next
		curr.next = prev
		prev = curr
		curr = tmp
	return prev # because curr is None, and prev is the new head (formerly tail)


from LINK import makeLL, printLL
a=[1,2,3,4,5,6,7]
head=makeLL(a)

printLL(A(head))