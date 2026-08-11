class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, e in enumerate(nums):
            if e in dict.values():
                return True
            dict[i] = e
        return False