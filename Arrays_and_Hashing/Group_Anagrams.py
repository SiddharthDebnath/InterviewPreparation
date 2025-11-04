from collections import defaultdict


def groupAnagrams(string):
    res = defaultdict(list)
    for s in string:
        sortedS = ''.join(sorted(s))
        print(sortedS)
        res[sortedS].append(s)
    return list(res.values())

def hashGroupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(hashGroupAnagrams(["a","b","c","a","b","c"]))