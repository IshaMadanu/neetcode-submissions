class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)

        sq = defaultdict(set) #r/3, c/3

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                board[row][col] in cols[col] or 
                board[row][col] in sq[row // 3, col//3]): 
                #is current num in curr row or col or sq
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                sq[row//3, col//3].add(board[row][col])
        return True


