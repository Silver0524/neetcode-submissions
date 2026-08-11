class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wmap = {}
        for word in strs:
            cmap = [0] * 26
            for letter in word:
                cmap[ord(letter) - 97] += 1
            wmap[tuple(cmap)] = wmap.get(tuple(cmap), []) + [word]
        return list(wmap.values())