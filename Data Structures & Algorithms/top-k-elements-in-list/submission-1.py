class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for val in nums:
            freqMap[val] = freqMap.get(val, 0) + 1
        sortedFreqMap = dict(sorted(freqMap.items(), key=lambda item: item[1], reverse=True))
        return list(sortedFreqMap.keys())[0:k]
        