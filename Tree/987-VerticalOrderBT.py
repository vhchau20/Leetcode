# Given a binary tree, return the vertical order traversal of its nodes values.

# For each node at position (X, Y), its left and right children respectively 
# will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the 
# vertical line touches some nodes, we report the values of the nodes in order 
# from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is 
# reported first is the value that is smaller.

# Return an list of non-empty reports in order of X coordinate.  Every report 
# will have a list of values of nodes.

# Example 1:
# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).

# Example 2:
# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according 
# to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is 
# smaller than 6.

# Note:
# The tree will have between 1 and 1000 nodes.
# Each node's value will be between 0 and 1000.

def A(root):
	# no tree
	if not root:
		return

	# Recursive function to populate hashmap
	def setCoord(node, d, x ,y):
		if not node:
			return
		# Map node's value to x,y coordinates
		d[node.val] = [x,y]
		# Use y+1 instead because easier to sort
		setCoord(node.left, d, x-1, y+1)
		setCoord(node.right, d, x+1, y+1)

	# Get coordinates for each node and sort by X coord
	d, sortedByX = {}, []
	setCoord(root, d, 0, 0)
	sortedByX = sorted(d.items(), key=lambda k: (k[1][0], k[1][1], k))
	print sortedByX

	# Add subarrays for each vertical to output array
	output, subArr = [], []
	# this loop is badly written but it works
	for i in sortedByX:
		if subArr and d[subArr[0]][0] != i[1][0]:
			output.append(subArr)
			subArr = []
		subArr.append(i[0])
	output.append(subArr)


	return output




from TREE import makeTree, printTreeRec
rootA=makeTree([1,2,3,4,5,6,7])
rootB=makeTree([3,9,20,None,None,15,7])

print A(rootA)

