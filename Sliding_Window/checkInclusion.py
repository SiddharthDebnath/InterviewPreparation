from collections import defaultdict

def checkInclusion(s1,s2):
    s1 = sorted(s1)

    for i in range(len(s2)):
        for j in range(i, len(s2)):
            subStr = s2[i: j + 1]
            subStr = sorted(subStr)
            if subStr == s1:
                return True
    return False

def hashMapCheckInclusion(s1,s2):
    count1 = defaultdict(int)
    for c in s1:
        count1[c] += 1

    need = len(count1)
    for i in range(len(s2)):
        count2, cur = {}, 0
        for j in range(i, len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            if count1.get(s2[j], 0) < count2[s2[j]]:
                break
            if count1.get(s2[j], 0) == count2[s2[j]]:
                cur += 1
            if cur == need:
                return True
    return False

print(checkInclusion("ab","abbc"))
