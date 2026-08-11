class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        lo = 0
        for val in nums:
            if len(window) > k:
                window.remove(nums[lo])
                lo += 1
            if val in window:
                return True
            window.add(val)
        return False