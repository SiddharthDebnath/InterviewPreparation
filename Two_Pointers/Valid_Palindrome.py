
def validPalindrome(arr):
    s = [char for char in arr if char.isalnum()]
    s = "".join(s)
    s = s.lower()
    n = len(s)
    left, right = 0, n - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def validPalindrome2(arr):
    s = [char for char in arr if char.isalnum()]
    s = "".join(s)
    s = s.lower()
    return True if s == s[::-1] else False


print(validPalindrome('was it a car or a cat i saw?'))
print(validPalindrome2('was it a car or a cat i saw?'))

