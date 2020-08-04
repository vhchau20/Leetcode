# Invert a binary tree.

# Example:

# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# main driver
def A(root):
	tmp = root
	helper(root)
	return tmp

# Post order traversal 
def helper(node):
	# base case
	if not node:
		return

	# post order recursion
	helper(node.left)
	helper(node.right)
	# Assign inverted nodes
	tmp = node.left
	node.left = node.right
	node.right = tmp

# Combine above two to get (LC SOLN)
def C(root):
	if not root:
		return None
	left = C(root.left)
	right = C(root.right)
	root.left = right
	root.right = left
	return root



def makeTree(arr):
	n = len(arr)
	treeArr = [0]*n
	for i in range(n):
		if arr[i]:
			treeArr[i] = TreeNode(arr[i],None,None)
		else:
			treeArr[i] = None
	for i in range(n):
		if not treeArr[i]:
			continue
		if 2*i+2 < n:
			treeArr[i].left = treeArr[2*i+1]
			treeArr[i].right = treeArr[2*i+2]
	return treeArr[0]

def printTree(root):
	if not root:
		return
	printTree(root.left)
	print root.val
	printTree(root.right)

arr = [4,2,7,1,3,6,9] # [4,7,2,9,6,3,1]
root = makeTree(arr)
node = C(root)
printTree(node)