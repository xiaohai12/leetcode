class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    count += 1
        return count

    def helper(self, grid, x, y):
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] != '1':
            return
        grid[x][y] = '#'
        self.helper(grid, x, y + 1)
        self.helper(grid, x, y - 1)
        self.helper(grid, x + 1, y)
        self.helper(grid, x - 1, y)
