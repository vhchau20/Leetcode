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
def C(intervals):
	intervals.sort(key=lambda x:x[0], reverse=True)
	sol = []
	while intervals: 
		if len(intervals) == 1:
			sol.append(intervals.pop())
			break

		# first = intervals[-1]
		while True:
			first = intervals[-1]
			if len(intervals) == 1:
				break
			second = intervals[-2]
			if first[1] >= second[0] or first == second:
				intervals.pop()
				intervals.pop()
				if first[1] >= second[1]:
					intervals.append([first[0], first[1]])
				else:
					intervals.append([first[0], second[1]])
				first = intervals[-1]
				continue
			else:
				break
		sol.append(intervals.pop())
	return(sol)

# O(nlogn)
def B(intervals):
	# O(nlogn)
    intervals.sort(key=lambda x: x[0])
    merged = []
    # O(n): Checks the merged list and sees whether its end time
    # is currently "separate" from i's start time or overlapping
    # If there's no overlap, append i
    # It there's overlap, then simply change the end time of merged's last
    # seen interval
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged

l1 = [[1,3],[2,6],[6,6],[8,10],[15,18]]
l2 = [[1,4],[4,5],[5,6]]
l3 = [[1,3],[2,6],[8,10],[15,18]]
l4 = [[1,3],[2,6],[5,10],[15,18],[19,20]]
l5 = [[1,4],[1,3],[5,10],[7,8],[9,11]]
l6 = [[1,10],[2,3],[4,10],[11,12],[13,14]]
l7 = [[1,4],[1,4],[1,4],[3,6]]
l8 = [[1,4],[1,4],[1,4],[1,4],[5,6]]
l9 = [[1,4],[1,4],[5,6]]
l10 = [[1,1],[2,6],[3,4],[7,8]]
# print(C(l1))
# print(C(l2))
# print(C(l3))
# print(C(l4))
# print(C(l5))
# print(C(l6))
# print(C(l7))
# print(C(l8))

# print l1[-1]
