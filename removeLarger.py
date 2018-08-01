#Given an unsorted array arr and a number n, delete all numbers in arr that are greater than n.
def removeLarger(arr, n):
    for i in arr:
        if i > n:
            arr.remove(i)
    return arr
list = [3, 4, 5, 6, 8, 9, 10, 452, 65, 2452, 75, 3424, 24, 563, 32, 445, 76, 87, 90, 34, 49, 12, 34]
a = removeLarger(list, 0)
print(a)
