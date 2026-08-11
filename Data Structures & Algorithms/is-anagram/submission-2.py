class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashOne, hashTwo = {}, {}
        for i in range(len(s)):
            hashOne[s[i]] = 1 + hashOne.get(s[i], 0)
            hashTwo[t[i]] = 1 + hashTwo.get(t[i], 0)
        for letter in hashOne:
            if hashOne[letter] != hashTwo.get(letter, 0):
                return False
        return True