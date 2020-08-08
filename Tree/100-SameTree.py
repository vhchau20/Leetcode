# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical 
# and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false


# Recursively represent each tree as an array using inorder traversal
# Check if arrays are equal
def A(p,q):
	pArr,qArr = [],[]
	h(p,pArr)
	h(q,qArr)
	pArr = [i.val if i else None for i in pArr]
	qArr = [i.val if i else None for i in qArr]
	return pArr==qArr

def h(n,arr):
	if not n:
		arr.append(None)
		return

	arr.append(n)
	h(n.left,arr)
	h(n.right,arr)


# Represent BT as array
from TREE import makeTree, printTree
p1=[1,2,3]
p2=[1,2,3]
a=makeTree(p1)
b=makeTree(p2)

print A(a[0],b[0])


