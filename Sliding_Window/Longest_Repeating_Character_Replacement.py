from collections import defaultdict

def bruteCharacterReplacement(s, k):
        res = 0
        for i in range(len(s)):
            count, maxf = defaultdict(int), 0
            for j in range(i, len(s)):
                count[s[j]] += 1
                maxf = max(maxf, count[s[j]])
                if (j-i+1) - maxf <=k:
                    res = max(res,j - i + 1)
        return res

def slidingWindowCharacterReplacement(s, k):
    res = 0
    charSet = set(s)

    for c in charSet:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1

            while (r - l + 1) - count > k:
                if s[l] == c:
                    count -= 1
                l += 1

            res = max(res, r - l + 1)
    return res

def OptimalSlidingWindowCharacterReplacement(s, k):
    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res


print(bruteCharacterReplacement("abbc", 2))
print(slidingWindowCharacterReplacement("abbc", 2))
print(OptimalSlidingWindowCharacterReplacement("abbc", 2))