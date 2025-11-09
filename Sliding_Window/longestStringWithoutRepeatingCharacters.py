def lengthOfLongestSubstring(s):
    seen = set()
    l = res = 0

    for r, ch in enumerate(s):
        while ch in seen:  # shrink window until duplicate removed
            seen.remove(s[l])
            l += 1
        seen.add(ch)
        res = max(res, r - l + 1)

    return res

def OptimalLengthOfLongestSubstring(s):
    mp = {}
    l = 0
    res = 0

    for r in range(len(s)):
        if s[r] in mp:
            l = max(mp[s[r]] + 1, l)
        mp[s[r]] = r
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring("abbc"))
print(OptimalLengthOfLongestSubstring("abbc"))