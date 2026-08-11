class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else:
                break
        
        row = matrix[mid]

        row_lo, row_hi = 0, len(row) - 1
        while row_lo <= row_hi:
            row_mid = row_lo + (row_hi - row_lo) // 2
            if row[row_mid] == target:
                return True
            elif row[row_mid] < target:
                row_lo = row_mid + 1
            else:
                row_hi = row_mid - 1
        return False