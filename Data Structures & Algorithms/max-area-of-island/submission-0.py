class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = self.explore(grid, i, j)
                    maxCount = max(count, maxCount)
        return maxCount


    def explore(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x][y] == 'x' or grid[x][y] == 0:
            return 0
    
        grid[x][y] = 'x' 
        
        count = 1
        count += self.explore(grid, x-1, y)
        count += self.explore(grid, x+1, y)
        count += self.explore(grid, x, y-1)
        count += self.explore(grid, x, y+1)
        
        return count
