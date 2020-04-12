class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == '':
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j):
                    return True
        return False

    def helper(self, board, word, i, j):
        if word == '':
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        opts = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        board[i][j] = '#'
        res = self.helper(board, word[1:], i + 1, j) or self.helper(board, word[1:], i - 1, j) or self.helper(board,
                                                                                                              word[1:],
                                                                                                              i,
                                                                                                              j + 1) or self.helper(
            board, word[1:], i, j - 1)

        board[i][j] = word[0]
        return res
