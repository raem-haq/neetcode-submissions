class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        while lo <= hi:
            sublistI = (lo + hi) // 2
            firstE = matrix[sublistI][0]
            if sublistI < len(matrix) - 1:
                compE = matrix[sublistI+1][0] ####
                if firstE <= target and compE > target:
                    break
                elif firstE > target:
                    hi = sublistI - 1
                else:
                    lo = sublistI + 1
            else:
                if firstE <= target:
                    break
                else:
                    hi = subListI - 1
        lo = 0
        hi = len(matrix[sublistI]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            n = matrix[sublistI][mid]
            if n == target:
                return True
            elif n < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
            
