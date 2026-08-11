class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            current = nums.pop(0)
            if current in nums:
                return True
            nums.append(current)
        return False