# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

def A(root):
	if not root:
		return
	arr = []
	depth = 0
	recur(root, depth, arr)
	return arr
	
def recur(node, depth, arr):
	if not node:
		return
	if len(arr) < depth+1:
		arr.append([])
	arr[depth].append(node.val)
	recur(node.left, depth+1, arr)
	recur(node.right, depth+1, arr)

from TREE import makeTree
a=[3,9,20,None,None,15,7]


print levelOrder(makeTree(a))