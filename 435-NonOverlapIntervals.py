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

# Does not work
# Basically find sets of overlapping intervals
def A(intervals):
	intervals.sort(key=lambda x:(x[0],x[1]))
	g = []
	i = j = 0
	while i < len(intervals):
		j = i+1
		c = []
		if j == len(intervals):
			c.append(intervals[i])
		while j < len(intervals):
			first = intervals[i]
			second = intervals[j]
			# Case 1 = no overlap
			if first[1] <= second[0]:
				pass
				if not c or c[-1] != first:
					c.append(first)
				return c
			# Case 2 = full overlap
			elif first[1] > second[0] and first[1] > second[1]:
				pass
				c.append(second)
			# Case 3 = partial overlap
			elif first[1] > second[0] and first[1] < second[1]:
				pass
				if not c or c[-1] != first:
					c.append(first)
				c.append(second)
				i = j
			j+=1 
		g.append(c)
		i+=1
	print g
	return


# Greedy Algo
# Heuristic: Choose interval with earliest end time
# O(n)
# compute the maximum set of non-overlapping intervals and 
# subtract from number of intervals
def B(intervals):
	count = 0
	time = float('-inf')
	for i in sorted(intervals,key=lambda x:x[1]):
		if i[0] >= time:
			time = i[1]
			count+=1
	return len(intervals)-count


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
m=[[1,10],[9,12],[11,13]]
n=[[1,5],[2,3],[4,7],[6,8],[9,10]]
o=[[1,5],[6,7]]
p=[[1,2],[1,2],[1,2]]


# print A(a)
# print A(b)
# print A(c)
# print A(d)
# print A(e)
# print A(f)
# print A(g)
# print A(h)
# print A(i)
# print A(j)

# print A(k)
# print A(l)
# print A(m)
# print A(n)
print B(l)


