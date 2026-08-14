class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        foundList = -1

        for x in range(len(matrix)):
            if matrix[x][0] <= target and matrix[x][len(matrix[x]) - 1] >= target:
                foundList = x
                break
        
        if foundList == -1:
            return False
        
        left = 0
        right = len(matrix[foundList]) - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[foundList][middle] == target:
                return True
            elif matrix[foundList][middle] < target:
                left = middle + 1
            elif matrix[foundList][middle] > target:
                right = middle - 1
        
        return False