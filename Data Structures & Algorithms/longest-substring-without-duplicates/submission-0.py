class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        l, r = 0, 1
        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            r += 1
            res = max(res, len(s[l:r]))
        return res