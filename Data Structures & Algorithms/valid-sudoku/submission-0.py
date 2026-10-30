class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_hash = collections.defaultdict(set)
        col_hash = collections.defaultdict(set)
        box_hash = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in row_hash[r] or
                    board[r][c] in col_hash[c] or
                    board[r][c] in box_hash[(r//3,c//3)]):

                    return False
                
                col_hash[c].add(board[r][c])
                row_hash[r].add(board[r][c])
                box_hash[(r//3,c//3)].add(board[r][c])

        return True