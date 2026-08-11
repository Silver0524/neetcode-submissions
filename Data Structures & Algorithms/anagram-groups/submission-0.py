class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            if key in freq:
                freq[key].append(word)
            else: 
                freq[key] = [word]
        return list(freq.values())