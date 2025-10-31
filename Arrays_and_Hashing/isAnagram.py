from collections import Counter


def bruteIsAnagram(s, t):
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False
    CountS = {}
    CountT = {}
    if len(s) != len(t):
        return False
    for i in s:
        if i in CountS:
            CountS[i] += 1
        else:
            CountS[i] = 1

    for i in t:
        if i in CountT:
            CountT[i] += 1
        else:
            CountT[i] = 1
    print(CountS)
    print(CountT)
    if CountS == CountT:
        return True
    else:
        return False




def sortedIsAnagram(s, t):
    if sorted(s.lower()) == sorted(t.lower()):
        return True

    else:
        return False

def counterIsAnagram(s, t):
    s = s.lower()
    t = t.lower()
    if Counter(s) == Counter(t):
        return True
    else:
        return False


print(bruteIsAnagram('Ship', 'Hips'))
print(sortedIsAnagram('Ship', 'Hips'))
print(counterIsAnagram('Ship', 'Hips'))
