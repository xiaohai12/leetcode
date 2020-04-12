class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != '.':
                    row.add(board[i][j])

                if board[j][i] in col:
                    return False
                elif board[j][i] != '.':
                    col.add(board[j][i])

        for i in range(3):
            for j in range(3):
                rec = set()
                for c in range(3 * i, 3 * i + 3):
                    for r in range(3 * j, 3 * j + 3):
                        if board[c][r] in rec:
                            return False
                        elif board[c][r] != '.':
                            rec.add(board[c][r])
        return True


    '''
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c,j),(i,c),(i/3,j/3,c)]
    return len(seen) == len(set(seen))
    '''