class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def makeTree(a):
	for i in range(len(a)):
		if a[i]: a[i] = Node(a[i])
	for i in range(len(a)):
		if 2*i+1 < len(a) and a[2*i+1]: a[i].left = a[2*i+1]
		if 2*i+2 < len(a) and a[2*i+2]: a[i].right = a[2*i+2]
	return a[0]

def printTreeArr(a):
	print [i.val for i in a if i]

def printTreeRec(root):
	if not root:
		return
	printTreeRec(root.left)
	print root.val
	printTreeRec(root.right)