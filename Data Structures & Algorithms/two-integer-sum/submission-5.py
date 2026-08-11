class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lmap = {}
        for i, v in enumerate(nums):
            if target - v in lmap.keys():
                return [lmap[target - v], i]
            lmap[v] = i