class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # search rows to find correct row
        b, t = 0, ROWS - 1
        while b <= t:
            mid = b + ((t - b) // 2)
            if target < matrix[mid][0]:
                t = mid - 1
            elif target > matrix[mid][COLS - 1]:
                b = mid + 1
            else:
                break

        # search in row to find target
        row = matrix[mid]
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False