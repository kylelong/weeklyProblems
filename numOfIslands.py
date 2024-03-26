def largestIsland(grid):
        max_size = float('-inf')
        num = 0
        rows, cols = len(grid), len(grid[0])

        def scan(grid, i, j, size):
            nonlocal max_size
            if i < 0 or j >= len(grid[0]) or i >= len(grid) or j < 0 or grid[i][j] == 0: return
            grid[i][j] = 0
            size += 1
            max_size = max(max_size, size)
            scan(grid, i + 1, j, size)
            scan(grid, i - 1, j, size)
            scan(grid, i, j - 1, size)
            scan(grid, i, j + 1, size)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num += 1
                    scan(grid, i, j, 1)
        return max_size if max_size != float('-inf') else 0

grid = [
    [0,1,1,1,0,0,0,1,1],
    [0,1,1,1,0,1,0,0,0],
    [0,1,0,0,0,0,0,1,0],
    [0,0,1,1,0,1,1,1,0],
]
assert(largestIsland(grid) == 7)