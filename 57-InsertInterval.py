# Given a set of non-overlapping intervals, insert a new interval 
# into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# NOTE: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.

# O(n): Same exact thing as 56`
def A(intervals, newInterval):
	intervals.append(newInterval)
	intervals.sort(key=lambda x:x[0], reverse=True)
	sol = []
	while len(intervals) != 0: 
		if len(intervals) == 1:
			sol.append(intervals.pop())
			break

		first = intervals[len(intervals)-1]
		while True:
			if len(intervals) == 1:
				break
			second = intervals[len(intervals)-2]
			if first[1] >= second[0] or first == second:
				intervals.pop()
				intervals.pop()
				if first[1] >= second[1]:
					intervals.append([first[0], first[1]])
				else:
					intervals.append([first[0], second[1]])
				first = intervals[len(intervals)-1]
				continue
			else:
				break
		sol.append(intervals.pop())
	return(sol)

# O(n) very fast but not space efficient at all
def B(intervals, newInterval):
	if not intervals:
		intervals.append(newInterval)
		return intervals
	overlap = []
	sol = []
	# Find all intervals overlapping with newInterval
	for i in intervals:
		if newInterval[0] <= i[1] and newInterval[1] >= i[0]:
			overlap.append(i)
	# Case where there are no overlapping intervals => just insert the 
	# newInterval but in sorted order
	if not overlap:
		# Case where new interval has earliest start and end time
		if newInterval[1] < intervals[0][0]:
			intervals.insert(0, newInterval)
			return intervals
		# Case where new interval has lates start and end time
		if newInterval[0] > intervals[-1][1]:
			intervals.append(newInterval)
			return intervals
		# Case where new interval is somewhere in middle
		sol.append(intervals[0])
		for i in range(1, len(intervals)):
			if newInterval[1] < intervals[i][0] and newInterval[0] > intervals[i-1][1]:
				sol.append(newInterval)
			sol.append(intervals[i])
	# Otherwise insert in replacement
	else:
		overlap.append(newInterval)
		replacement = [min(i[0] for i in overlap),max(i[1] for i in overlap)]
		for i in intervals:
			if newInterval[0] <= i[1] and newInterval[1] >= i[0]:
				# Case where overlapping intervals were at beginning
				if not sol:
					sol.append(replacement)
					continue
				# Case where overlapping middles were  in the middle/end
				if sol[-1] != replacement:
					sol.append(replacement)
			else:
				sol.append(i)
	return sol


# print(B([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,12]))
# print(B([[1,3],[6,9]], [2,5]))
# print(B([[1,2],[3,4],[9,10]], [6,8]))
# print(B([[3,5],[12,15]],[6,6]))
# print(B([[3,4],[5,6]],[1,2]))
# print(B([[1,2],[3,4]],[5,6]))


class interval:
	def __init__(self, start=0, end=0):
		self.start = start
		self.end = end



def D(intervals, newInterval):
        res = []
        i = 0
        #skip all intervals that come before new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        #merge all intervals that overlap with new interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        
        #add all remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res











