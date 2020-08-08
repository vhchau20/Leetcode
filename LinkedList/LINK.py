class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def makeLL(a):
	for i in range(len(a)):
		a[i] = Node(a[i])
	for i in range(len(a)-1):
		a[i].next = a[i+1]
	return a[0]

def getTail(head):
	while head.next:
		head = head.next
	return head

def printLL(head):
	while head:
		print head.val
		head = head.next