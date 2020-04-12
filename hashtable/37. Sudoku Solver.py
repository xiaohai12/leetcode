class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        self.solver(board)

    def solver(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        c = str(c)
                        if self.valid(board, i, j, c):
                            board[i][j] = c
                            if self.solver(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def valid(self, board, i, j, c):
        for row in range(9):
            if board[row][j] == c:
                return False
        for col in range(9):
            if board[i][col] == c:
                return False
        r = int(i / 3)
        t = int(j / 3)
        for row in range(3 * r, 3 * r + 3):
            for col in range(3 * t, 3 * t + 3):
                if board[row][col] == c:
                    return False
        return True
