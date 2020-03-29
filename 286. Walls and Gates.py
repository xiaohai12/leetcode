class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])
        Queue = collections.deque()

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    Queue.appendleft((i, j))

        while Queue:
            top = Queue.pop()
            row = top[0]
            col = top[1]

            if row - 1 > 0 and rooms[row - 1][col] == 2 ** 31 - 1:
                rooms[row - 1][col] = 1 + rooms[row][col]
                Queue.appendleft(row - 1, col)

            if col - 1 > 0 and rooms[row][col - 1] == 2 ** 31 - 1:
                rooms[row][col - 1] = 1 + rooms[row][col]
                Queue.appendleft(row, col - 1)

            if row + 1 < n and rooms[row + 1][col] == 2 ** 31 - 1:
                rooms[row + 1][col] = 1 + rooms[row][col]
                Queue.appendleft(row + 1, col)

            if col + 1 > 0 and rooms[row][col + 1] == 2 ** 31 - 1:
                rooms[row][col + 1] = 1 + rooms[row][col]
                Queue.appendleft(row, col + 1)
        return rooms