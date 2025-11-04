from collections import defaultdict

def bruteTwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target :
                return i, j

def twoPassHaspMapTwoSum(nums, target):
    indices = defaultdict(int)

    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]

def onePassHaspMapTwoSum(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

def sortedTwoSum(nums, target):
    A = []
    for i, num in enumerate(nums):
        A.append([num, i])

    A.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        cur = A[i][0] + A[j][0]
        if cur == target:
            return [min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []

print(bruteTwoSum([1,2,3,4,5,6,7,8,9], 9))
print(twoPassHaspMapTwoSum([1, 2, 3, 4], 4))
print(onePassHaspMapTwoSum([1, 2, 3, 4], 6))
print(sortedTwoSum([1,2,3,4,5,6,7,8,9], 9))
