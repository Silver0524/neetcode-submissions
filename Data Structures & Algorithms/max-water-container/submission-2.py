class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            if heights[l] < heights[r]:
                if area < (r - l) * heights[l]:
                    area = (r - l) * heights[l]
                l += 1
            else:
                if area < (r - l) * heights[r]:
                    area = (r - l) * heights[r]
                r -= 1
            
        return area