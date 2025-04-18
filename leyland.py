def leyland(n: int):
    numbers = []
    x, y = 2, 2
    while n > 0:
        numbers.append(x ** y + y ** x)
        n -= 1
        
    return numbers
print(leyland(1))