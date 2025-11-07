
def bruteForceThreeSum(arr):
    result = set()
    for num in arr:
        for num2 in arr:
            for num3 in arr:
                if num !=num2 & num2!= num3 & num!=num3 & num + num2 == -num3:
                    result.add([arr[num],arr[num2],arr[num3]])
    return set(result)

print(bruteForceThreeSum([-1, 0, 1, 2, -1, -4]))

