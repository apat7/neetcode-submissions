class Solution:
    def explore(self, x, y, grid):
        grid[x][y] = "x"
        if x < len(grid)-1:
            if grid[x+1][y] == "1":
                self.explore(x+1, y, grid)
        if y < len(grid[x])-1:
            if grid[x][y+1] == "1":
                self.explore(x, y+1, grid)
        if x > 0:
            if grid[x-1][y] == "1":
                self.explore(x-1, y, grid)
        if y > 0:
            if grid[x][y-1] == "1":
                self.explore(x, y-1, grid)
        return
            
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    count += 1
                    self.explore(x, y, grid)
        return count