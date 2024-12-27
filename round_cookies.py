from math import factorial

def countPerfectlyRoundCookies(num):
    return zeroes(factorial(num))

def zeroes(num):
    count = 0
    while num % 10 == 0:
        count += 1
        num //= 10
    return count

assert countPerfectlyRoundCookies(5) == 1
assert countPerfectlyRoundCookies(10) == 2
assert countPerfectlyRoundCookies(100) == 24