class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        res = []
        while count < len(word1) and count < len(word2):
            res.append(word1[count])
            res.append(word2[count])
            count += 1
        res.append(word1[count:])
        res.append(word2[count:])
        return "".join(res)