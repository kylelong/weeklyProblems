
def findShieldBreak(damages, capacity):
    return next((i for i in range(len(damages)) if sum(damages[:i+1]) >= capacity), -1)

assert findShieldBreak([10, 20, 30, 40], 50) == 2
assert findShieldBreak([1, 2, 3, 4], 20) == -1
assert findShieldBreak([50], 30) == 0
assert findShieldBreak([500, 300, 1000, 400], 650) == 1