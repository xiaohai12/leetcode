class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        index_list = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, word, i, j, index_list):
                    return True
        return False

    def backtrack(self, board, word, row, col, index_list):
        ret = False
        if word == '':
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        if board[row][col] == word[0] and index_list[row][col] == False:
            index_list[row][col] = True
            ret = self.backtrack(board, word[1:], row + 1, col, index_list) or self.backtrack(board, word[1:], row - 1,
                                                                                              col, index_list) \
                  or self.backtrack(board, word[1:], row, col + 1, index_list) or self.backtrack(board, word[1:], row,
                                                                                                 col - 1, index_list)
            index_list[row][col] = False
        return ret


