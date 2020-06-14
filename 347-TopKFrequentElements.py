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


def topKFrequent(nums,k):
    A = {}
    B = [0]*k
    for i in nums:
        if i in A:
            continue
        A[i] = 0
    for i in nums:
        A[i] += 1
    invA = {v: k for k, v in A.items()}
    listValues = list(invA)
    decValues = sorted(listValues,reverse=True)
    for i in range(k):
        B[i] = invA[decValues[i]]
    print(A)
    return(A)

topKFrequent([1,1,1,2,2,3],2)