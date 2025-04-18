from typing import List
def gridSum(grid: List[List[int]]) -> int:
    total = 0
    res = float('-inf')
    
    def helper(grid: List[List[int]], r: int, c: int, s):
        nonlocal total
        nonlocal res
        pair = (r,c)
        if pair in s or  r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 
        total += grid[r][c]
        if total > res:
            res = total
        s.add(pair)
        helper(grid, r + 1, c,s)
        helper(grid, r, c + 1,s)
        helper(grid, r - 1, c,s)
        helper(grid, r, c - 1,s)
        total -= grid[r][c]
        
    helper(grid, 0, 0, set())
    return res

grid1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
grid2 = [
  [5, 3],
  [2, 8]
];
assert gridSum(grid1) == 45
assert gridSum(grid2) == 18