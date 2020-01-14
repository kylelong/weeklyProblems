#Cassido's newsletter interview of the week 1/14
def isPalindrome(num):
    word = str(num)
    return word == word[::-1]
def nPalindrome(num):
    sum = 0
    start = 10 ** (num - 1)
    end = 10 ** num
    for i in range(start, end):
        if isPalindrome(i):
            sum = sum + i
    return sum
print(nPalindrome(2))