class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for val in nums:
            if val > nums[l]:
                l += 1
                nums[l] = val
        return l + 1