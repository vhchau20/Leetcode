# # Given a binary tree, find its maximum depth.

# # The maximum depth is the number of nodes along the longest 
# # path from the root node down to the farthest leaf node.

# # Note: A leaf is a node with no children.

# # Example:

# # Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def A(root):
	return max(A(root.left),A(root.right))+1 if root != None else 0

# BFS
def B(root):
	depth = 0
	level = [root] if root else []
	while level:
		depth += 1
		queue = []
		for el in level:
			if el.left:
				queue.append(el.left)
			if el.right:
				queue.append(el.right)
		level = queue
	return depth

# DFS
def C(root):
	depth=0
	stack = [(root,1)]
	while stack:
		root,leng=stack.pop()
		if not root:
			return 0
		if leng > depth:
			depth = leng
		if root.right:
			stack.append((root.right,leng+1))
		if root.left:
			stack.append((root.left,leng+1)) 
	return depth

tree = [3,9,20,None,None,15,7]
tree = [3,None,20,None,None,None,7]
nodes = []
for i in tree:
	if i != None:
		nodes.append(TreeNode(i,None,None))
	else:
		nodes.append(None)
for i in range(len(nodes)):
	if nodes[i] == None:
		continue
	if 2*i+2 < len(nodes):
		nodes[i].left = nodes[2*i+1]
	if 2*i+2 < len(nodes):
		nodes[i].right = nodes[2*i+2]

print A(nodes[0])