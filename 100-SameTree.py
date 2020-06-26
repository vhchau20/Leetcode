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
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

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


p1=[1,None,2]
p2=[1,2]

nodes1=[]
nodes2=[]

for i in p1:
	if i != None:
		nodes1.append(TreeNode(i,None,None))
	else:
		nodes1.append(None)
for i in p2:
	if i != None:
		nodes2.append(TreeNode(i,None,None))
	else:
		nodes2.append(None)

for i in range(len(nodes1)):
	if nodes1[i] == None:
		continue
	if 2*i+2 < len(nodes1):
		nodes1[i].left = nodes1[2*i+1]
	if 2*i+2 < len(nodes1):
		nodes1[i].right = nodes1[2*i+2]

for i in range(len(nodes2)):
	if nodes2[i] == None:
		continue
	if 2*i+2 < len(nodes2):
		nodes2[i].left = nodes2[2*i+1]
	if 2*i+2 < len(nodes2):
		nodes2[i].right = nodes2[2*i+2]

print [i.val if i else None for i in nodes1]
print [i.val if i else None for i in nodes2]
print A(nodes1[0],nodes2[0])

