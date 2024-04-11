# https://buttondown.email/cassidoo/subscribers/14e61a74-5e22-45c0-9830-53f7028da509/archive/7-you-have-to-care-about-your-work-but-not-about 
from itertools import permutations

def diceSum(n,m,target):
    sides = [i for i in range(1, m + 1)]
    rolls = list(permutations(sides, n))
    res = 0
    for r in rolls:
        if sum(r) == target: res += 1
    return res

assert(diceSum(1,6,3) == 1)
assert(diceSum(2,6,7) == 6)