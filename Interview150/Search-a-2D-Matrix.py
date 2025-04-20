class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # (0,0) -> 0
        # (m-1,n-1) -> m*n - 1
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        r = m*n - 1
        while l<=r:
            mid = (l+r) // 2
            x = mid // n
            y = mid % n
            # print(f\mid:{m} x:{x} y:{y}\)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid+1
            else:
                r = mid-1
        return False


        