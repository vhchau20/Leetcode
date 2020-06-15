# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:
# You may assume k is always valid, 1<=k<= number of unique elements
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.

# O(nlogk) using naive sorting
def topKFrequent(nums,k):
    A = {}
    for i in nums:
        A[i] = A.get(i,0) + 1
    # Sort dict by values in increasing order
    B = sorted(list(A.items()), key=lambda k:k[1]) # nlogk
    print("counts:", A)
    print("dict in increasing order by values", B)
    sol = []
    for i in range(k):
        sol.append(B.pop()[0])
    print(sol)

# O(n)? using heap
import heapq
def topKFrequent2(nums,k):
    A = {}
    for i in nums:
        A[i] = A.get(i,0) + 1
    heap = []
    for i in A:
        heapq.heappush(heap, (A[i],i))
    print(heap)
    sol = []
    for i in range(k):
        sol.append(heap.pop()[1])
    print(sol)



arr = [3,3,2,2,1,4,4,4]
topKFrequent2(arr,3)
