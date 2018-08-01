def mergeArray(arr):
    l = []
    size = len(arr)
    for i in range(size):
        for x in range(len(arr[i])):
            l.append(arr[i][x])
    print(l)
# arr = [[1, 3], [2, 4, 5], [0, 9, 10, 11]]
# mergeArray(arr)