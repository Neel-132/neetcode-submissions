class Solution:
    def check_row_validity(self, board:List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in visited:
                    return False
                else:
                    visited.add(board[i][j])

        return True
    def check_column_validity(self, board:List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in visited:
                    return False
                else:
                    visited.add(board[j][i])

        return True
        
    def check_subbox_validity(self, board: List[List[str]]) -> bool:
        for a in range(3):
            for b in range(3):
                visited = set()
                if a % 2 == 0:
                    i = 3 * a
                else:
                    i = 2 * a + 1
                if b % 2 == 0:
                    j = 3 * b
                else:
                    j = 2 * b + 1

                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] == '.':
                            continue
                        if board[i + k][j + l] in visited:
                            print(i + k, j + l, a, b, visited) 
                            return False
                        else:
                            visited.add(board[i + k][j + l])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_row_validity(board) and self.check_column_validity(board) and self.check_subbox_validity(board)

                
                
        