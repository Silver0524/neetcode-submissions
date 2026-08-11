class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_one = {}
        freq_two = {}
        for letter in s:
            freq_one[letter] = freq_one.get(letter, 0) + 1
        for letter in t:
            freq_two[letter] = freq_two.get(letter, 0) + 1
        return freq_one == freq_two