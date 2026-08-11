class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for key, val in enumerate(nums):
            if target - val not in d:
                d[val] = key
            else:
                return [d[target-val], key]