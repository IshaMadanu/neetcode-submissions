class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #binary search among rows, check first and last elem to see if target could be in btwn them
        topRow = 0
        bottomRow = len(matrix) - 1 

        while topRow <= bottomRow:
            row = (topRow + bottomRow) // 2
            if matrix[row][0] > target:
                bottomRow = row - 1
            elif matrix[row][-1] < target:
                topRow = row + 1
            else: #if it is, then binary search among that row, otherwise check row above or below it
                break
            
        
        if not (topRow <= bottomRow):
            return False #no valid row is found


        #binary search among valid range row
        # row = (topRow + bottomRow) // 2
        low, high = 0, len(matrix[0]) - 1

        while low <= high:
            col = (low + high) // 2
            if target > matrix[row][col]:
                low = col + 1
            elif target < matrix[row][col]:
                high = col - 1
            else:
                return True

        return False