import math
def betweenNums(a, b, mode):
    start, end = sorted([a,b])
    def isPrime(n):
        if n <= 1: return False
        high = int(math.sqrt(n)) + 1
        for i in range(2, high):
            if n % i == 0:
                return False
        return True

    if mode == "even":
        return [x for x in range(start, end) if x % 2 == 0]
    elif mode == "odd":
        return [x for x in range(start, end + 1) if x % 2 == 1]
    else:
        return [x for x in range(start, end) if isPrime(x)]
print(betweenNums(3, 11, 'even'))
print(betweenNums(15, 1, 'prime'))

