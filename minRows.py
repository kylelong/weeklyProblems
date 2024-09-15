
def minRows(groups, rowSize):
    groups.sort()
    minRows = 0
    index = len(groups) - 2
    curr_sum = groups[-1]

    while index >=0 :
        curr = groups[index]
        if curr + curr_sum >= rowSize:
            minRows += 1
            curr_sum = curr
        else:
            curr_sum += curr
        index -= 1
    if groups[0] + groups[1] > rowSize : minRows += 1
    return minRows
    
assert minRows([4, 8, 3, 5, 6], 10) == 3
assert minRows([4, 5, 4, 3, 3], 10) == 2
assert minRows([7, 7, 8, 9, 6], 10) == 5


