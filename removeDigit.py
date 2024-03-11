# Given a number and a digit to remove from that number, maximize the resulting number after the digit has been removed and print it.
def removeDigit(num, digit):
    number, index, indices = [], len(str(num)) - 1, []
    ans = float("-inf")
    
    while num != 0:
        number.insert(0, num % 10)
        if num % 10 == digit: indices.append(index)
        num = num // 10
        index -= 1
    

    for i in indices:
        copy = number.copy()
        copy.pop(i)
        l = list(map(str,copy))
        num = int("".join(l))
        ans = max(num, ans)
    return ans
removeDigit(31415926, 1) # 3415926
removeDigit(1231, 1) # 231