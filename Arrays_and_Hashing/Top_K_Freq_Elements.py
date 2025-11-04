from collections import Counter, defaultdict
import heapq


def sortedTopKFrequent(nums, k):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


def minHeapTopKFrequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res

def bucketsortTopKFrequent(nums, k):
    count = defaultdict(int)
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] += 1
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

print(sortedTopKFrequent([1,2,2,3,3,3], 2))
print(minHeapTopKFrequent([1,2,2,3,3,3], 2))
print(bucketsortTopKFrequent([1,2,2,3,3,3], 2))