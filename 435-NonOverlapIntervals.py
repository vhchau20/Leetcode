# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:

# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:

# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Note:

# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


class interval:
	def __init__(self, start=0, end=0):
		self.start = start
		self.end = end

def A(intervals):
	intervals.sort(key=lambda x:(x[0],x[1]))
	print intervals
	g = []
	i = j = 0
	while i < len(intervals):
		j = i+1
		c = []
		while j < len(intervals):
			first = intervals[i]
			second = intervals[j]
			# Case 1 = no overlap
			if first[1] <= second[0]:
				pass
				c.append(first)
			# Case 2 = full overlap
			if first[1] > second[0] and first[1] > second[1]:
				pass
				c.append(second)
			# Case 3 = partial overlap
			if first[1] > second[0] and first[1] < second[1]:
				pass
				c.append(second)
			j+=1 
		g.append(c)
		i+=1
	return len(g)


# a=[[1,2],[1,2],[2,3],[3,4],[1,3]] # = 2
# b=[[1,3],[1,2],[2,3],[3,4],[1,3]] # = 2
# c=[[1,4],[4,5],[5,6]] # = 0
# d=[[1,3],[2,6],[8,10],[15,18]] # = 1
# e=[[1,3],[2,6],[5,10],[15,18],[19,20]] # = 1
# f=[[1,4],[1,3],[5,10],[7,8],[9,11]] # = 2
# g=[[1,10],[2,3],[4,10],[11,12],[13,14]] # = 1
# h=[[1,4],[1,4],[1,4],[3,6]] # = 3
# i=[[1,4],[1,4],[1,4],[1,4],[5,6]] # = 3
# j=[[1,4],[1,4],[5,6]] # = 1

k=[[1,10],[2,3],[4,5],[8,12],[9,14],[15,16]]
l=[[1,10],[2,3],[4,5],[8,12],[9,14],[13,16],[17,18]] # = 2
# print A(a)
# print A(b)
# print A(c)
# print A(d)
# print A(e)
print A(l)
# print A(g)
# print A(h)
# print A(i)
# print A(j)