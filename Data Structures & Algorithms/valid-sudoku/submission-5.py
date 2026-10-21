class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        # check column
        # check 3 by 3 grid
        # time: O(N^2) - n is grid size (n is 9 in this case)
        # space: O(N)
        
        # for i in range(9):
        #     row = set()
        #     col = set()
        #     for j in range(9):
        #         if board[i][j] in row:
        #             return False
        #         if board[j][i] in col:
        #             return False

        #         if board[i][j] != ".":
        #             row.add(board[i][j])
        #         if board[j][i] != ".":
        #             col.add(board[j][i])

        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         grid = set()
        #         for x in range(i, i+3, 1):
        #             for y in range(j, j+3, 1):
        #                 if board[x][y] in grid:
        #                     return False
                        
        #                 if board[x][y] != ".":
        #                     grid.add(board[x][y])

        # return True 

        # one pass
        # time: O(N^2)
        # space" O(N^2)
        # // is how we get the subgrid start coordinates
        col = defaultdict(set)
        row = defaultdict(set)
        subGrid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]

                if n == ".":
                    continue
                subGridCoord = (r//3, c//3)
                if (n in row[r] 
                    or n in col[c] 
                    or n in subGrid[subGridCoord]):
                    return False

                col[c].add(n)
                row[r].add(n)
                subGrid[(subGridCoord)].add(n)
        
        return True


