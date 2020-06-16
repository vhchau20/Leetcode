# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.


# O(n^2)
def A(intervals):
	sol = []
	intervals.sort(key=lambda x: x[0])
	i = 0
	k = 0
	while i < len(intervals):
		i = k
		newInterval = intervals[i]
		j = i+1
		while j < len(intervals):
			if  intervals[i][1] >= intervals[j][0] and intervals[i][1] < intervals[j][1]:
				newInterval[1] = intervals[j][1]
				i = j
			elif intervals[i][1] < intervals[j][0]:
				k = j
				break
			elif intervals[i] == intervals[j]:
				pass
			j+=1
		sol.append(newInterval)
		i+=1
	return sol

l1 = [[1,3],[2,6],[8,10],[15,18]]
l2 = [[1,4],[4,5],[5,6]]
l3 = [[8,10],[15,18],[1,3],[2,6]]
l4 = [[1,3],[2,6],[5,10],[15,18],[19,20]]
l5 = [[1,4],[2,3],[5,10],[7,8],[9,11]]
l6 = [[1,10],[2,3],[4,10],[11,12],[13,14]]
l7 = [[1,4],[1,4]]

# print(A(l1))
# print(A(l2))
# print(A(l3))
# print(A(l4))
# print(A(l5))
# print(A(l6))
# print(A(l7))
print([1,2] == [1,2])
