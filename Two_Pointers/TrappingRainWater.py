def bruteForceTrap(height):
    if not height:
        return 0
    n = len(height)
    res = 0

    for i in range(n):
        leftMax = rightMax = height[i]

        for j in range(i):
            leftMax = max(leftMax, height[j])
        for j in range(i + 1, n):
            rightMax = max(rightMax, height[j])

        res += min(leftMax, rightMax) - height[i]
    return res

def prefixSuffixSumTrap(heights):
    n = len(heights)
    if n == 0:
        return 0

    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = heights[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], heights[i])

    rightMax[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], heights[i])

    res = 0
    for i in range(n):
        res += min(leftMax[i], rightMax[i]) - heights[i]
    return res

def stackTrap(heights):
    if not heights:
        return 0
    stack = []
    res = 0

    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            mid = heights[stack.pop()]
            if stack:
                right = heights[i]
                left = heights[stack[-1]]
                h = min(right, left) - mid
                w = i - stack[-1] - 1
                res += h * w
        stack.append(i)
    return res


def TwoPointertrap(height):
    if not height:
        return 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res



print(prefixSuffixSumTrap([1, 0, 1, 2, 1, 4]))
print(TwoPointertrap([0,2,0,3,1,0,1,3,2,1]))
print(stackTrap([0,2,0,3,1,0,1,3,2,1]))
