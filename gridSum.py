from typing import List, Set, Tuple

def gridSum(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()
    max_sum = float('-inf')

    def dfs(r: int, c: int, total: int):
        nonlocal max_sum
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols):
            return
        total += grid[r][c]
        max_sum = max(max_sum, total)
        visited.add((r, c))
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dfs(r + dr, c + dc, total)
        visited.remove((r, c))

    dfs(0, 0, 0)
    return max_sum


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