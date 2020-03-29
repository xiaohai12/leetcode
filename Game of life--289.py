class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        flag = [[False for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                s = 0
                for k in range(max(i - 1, 0), min(i + 2, n)):
                    for k2 in range(max(j - 1, 0), min(j + 2, m)):
                        s += board[k][k2]

                if board[i][j] == 0:
                    if s == 3:
                        flag[i][j] = True
                else:
                    if s > 3 + 1 or s < 2 + 1:
                        flag[i][j] = True

        for i in range(n):
            for j in range(m):
                if flag[i][j]:
                    board[i][j] = (board[i][j] + 1) % 2
