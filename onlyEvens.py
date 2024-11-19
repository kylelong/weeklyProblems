# onlyEvens = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,2]))
def onlyEvens(numbers):
    return [x for x in numbers if x % 2 == 0]
print(onlyEvens([1,2,3,2,4,5]))