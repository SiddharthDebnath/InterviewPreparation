
def bruteContainsDuplicate(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def hashMapContainsDuplicate(nums):
    container = {}
    for i in nums:
        if i in container:
            return True
        else:
            container[i] = 1
    return False

def sortedArrayContainsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

def setContainsDuplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True

print(bruteContainsDuplicate([1, 2, 3, 1]))
print(hashMapContainsDuplicate([1, 2, 3]))
print(sortedArrayContainsDuplicate([1, 2, 3]))
print(setContainsDuplicate([1, 2, 3, 6]))
