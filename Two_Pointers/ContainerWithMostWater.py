def maxArea(heights):
    left = 0
    right = len(heights) - 1
    maxWater = 0
    while left < right:
        maxWater = max(maxWater,(right - left)*min(heights[left], heights[right]))
        if heights[left] >= heights[right]:
            right -= 1
        else:
            left += 1
    return maxWater

def optimalMaxArea(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - i))
    return res

print(optimalMaxArea([1,7,2,5,4,7,3,6]))
print(maxArea([1,7,2,5,4,7,3,6]))