class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x
        
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                lo = mid + 1
            elif mid * mid > x:
                hi = mid
        return lo - 1