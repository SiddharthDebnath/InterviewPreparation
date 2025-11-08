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

print(lengthOfLongestSubstring("abcabcbb"))