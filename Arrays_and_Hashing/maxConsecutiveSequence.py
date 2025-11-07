def longestConsecutiveSequence(nums):
    longest = 1
    current = 1

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue  # skip duplicates
        elif nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1

    return max(longest, current)

print(longestConsecutiveSequence([0,3,2,5,4,6,1,1]))