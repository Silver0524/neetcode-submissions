class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lo, row_hi = 0, len(matrix) - 1
        while (row_lo <= row_hi):
            row_mid = (row_lo + row_hi) // 2
            if (target < matrix[row_mid][0]):
                row_hi = row_mid - 1
            elif (target > matrix[row_mid][-1]):
                row_lo = row_mid + 1
            else:
                # binary search inside each row
                lo, hi = 0, len(matrix[row_mid]) - 1
                while (lo <= hi):
                    mid = (lo + hi) // 2
                    if (matrix[row_mid][mid] == target):
                        return True
                    elif (matrix[row_mid][mid] < target):
                        lo = mid + 1
                    else:
                        hi = mid - 1
                return False
        return False
