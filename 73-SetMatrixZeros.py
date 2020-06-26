# Given a m x n matrix, if an element is 0, 
# set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?



def A(matrix):
	r = len(matrix)
	c = len(matrix[0])
	indexForZeroes = []

	for i in range(r):
		for j in range(c):
			if matrix[i][j] == 0:
				indexForZeroes.append([i,j])

	for i in indexForZeroes:
		matrix[i[0]] = [0]*c
		for j in matrix:
			j[i[1]] = 0

	return matrix


def setZeroes(matrix):
	MODIFIED = -1000000
	R = len(matrix)
	C = len(matrix[0])
	for r in range(R):
		for c in range(C):
			if matrix[r][c] == 0:
				# We modify the elements in place. Note, we only change the non zeros to MODIFIED
				for k in range(C):
					matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
				for k in range(R):
					matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
	for r in range(R):
		for c in range(C):
			# Make a second pass and change all MODIFIED elements to 0 """
			if matrix[r][c] == MODIFIED:
				matrix[r][c] = 0

def setZeroes(self, matrix):
	is_col = False
	R = len(matrix)
	C = len(matrix[0])
	for i in range(R):
		# Since first cell for both first row and first column is the same i.e. matrix[0][0]
		# We can use an additional variable for either the first row/column.
		# For this solution we are using an additional variable for the first column
		# and using matrix[0][0] for the first row.
		if matrix[i][0] == 0:
			is_col = True
		for j in range(1, C):
			# If an element is zero, we set the first element of the corresponding row and column to 0
			if matrix[i][j]  == 0:
				matrix[0][j] = 0
				matrix[i][0] = 0

	# Iterate over the array once again and using the first row and first column, update the elements.
	for i in range(1, R):
		for j in range(1, C):
			if not matrix[i][0] or not matrix[0][j]:
				matrix[i][j] = 0

	# See if the first row needs to be set to zero as well
	if matrix[0][0] == 0:
		for j in range(C):
			matrix[0][j] = 0

	# See if the first column needs to be set to zero as well        
	if is_col:
		for i in range(R):
			matrix[i][0] = 0

a=[
[1,1,0,1],
[3,4,0,2],
[1,3,1,5]
]

print A(a)
