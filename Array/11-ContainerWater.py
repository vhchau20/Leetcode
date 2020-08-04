# Given n non-negative integers a1, a2, ..., an , where each represents
# a point at coordinate (i, ai). n vertical lines are drawn such that
# the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container, such that the container
# contains the most water.

# Note: You may not slant the container and n is at least 2.

# naive n2
def A(height):
	n = len(height)

	maxArea = 0

	for i in range(n):
		for j in range(i,n):
			diff = j-i
			minHeight = min(height[i],height[j])
			area = minHeight * diff
			if area > maxArea:
				maxArea = area

	return maxArea

def B(height):
	n = len(height)
	p1,p2 = 0,n-1
	maxArea = 0

	while p1<p2:
		# Get area
		diff = p2-p1
		minHeight = min(height[p1],height[p2])
		area = minHeight*diff
		if area > maxArea:
			maxArea = area

		# Move pointers
		if height[p2] < height[p1]:
			p2 -= 1
		elif height[p1] < height[p2]:
			p1 += 1
		elif height[p1] == height[p2]:
			p1 += 1

	return maxArea

a=[12,8,6,2,5,4,12,3,7]
print A(a)