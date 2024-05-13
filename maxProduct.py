def maxProduct(a):
    if len(a) < 3: return 0
    a.sort()
    return max(a[0] * a [1] * a[-1], a[-3] * a[-2] * a[-1])

assert(maxProduct([2, 4, 1, 3, -5, 6]) == 72)
assert(maxProduct([43,100]) == 0)
assert(maxProduct([95]) == 0)
assert(maxProduct([]) == 0)
assert(maxProduct([-1, -2, -3, -4, -5]) == -6)
assert(maxProduct([-10, -10, 1, 3, 2]) == 300)