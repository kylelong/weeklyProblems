from typing import List

def findLongestStreak(values: List[bool], goal:int ) -> int:
    longest, l = -1, 0
    for r in range(len(values)):
        if values[r] == False:
            l = r + 1
        longest = max(longest, r - l + 1)
    return 0 if longest < goal else longest

assert findLongestStreak([True, True, False, True, True, True], 3) == 3
assert findLongestStreak([True, True, True, False, True], 4) == 0
assert findLongestStreak([True, True, True, True], 2) == 4