class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_set = defaultdict(set)
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])

        
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_set:
                    return False
                else:
                    col_set.add(board[j][i])

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in box_set[(i//3,j//3)]:
                    return False
                else:
                    box_set[(i//3, j//3)].add(board[i][j])

        return True
