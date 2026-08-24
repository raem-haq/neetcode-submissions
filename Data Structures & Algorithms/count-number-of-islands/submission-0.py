class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        code = 0
        visit = set()
        ROWS, COL = len(grid), len(grid[0])
        

        def dfs(r, c):
            if r < ROWS and r >= 0 and c >=0 and c < COL and grid[r][c] == "1" and (r,c) not in visit:
                visit.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c)
                    code += 1
        return code