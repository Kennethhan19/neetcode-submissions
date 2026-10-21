class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        # check column
        # check 3 by 3 grid
        
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                if board[j][i] in col:
                    return False

                if board[i][j] != ".":
                    row.add(board[i][j])
                if board[j][i] != ".":
                    col.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = set()
                for x in range(i, i+3, 1):
                    for y in range(j, j+3, 1):
                        if board[x][y] in grid:
                            return False
                        
                        if board[x][y] != ".":
                            grid.add(board[x][y])
                            
        return True 
