def seeBuildingsLeft(buildings):
    tallest = res = 0
    for num in buildings:
        tallest = max(tallest, num)
        res = res + 1 if num == tallest else res
    return res

assert seeBuildingsLeft([1,2,3,4,5]) == 5
assert seeBuildingsLeft([5,4,3,2,1]) == 1
assert seeBuildingsLeft([3,7,8,3,6,1]) == 3
assert seeBuildingsLeft([1,2,6,4,9]) == 4