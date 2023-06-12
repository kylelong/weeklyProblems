def trimArray(numbers, start, last)
    last == 0 ? numbers[start..] : numbers[start...-last]
end
p trimArray([1, 2, 3, 4, 5, 6], 2, 1) # [3, 4, 5]
p trimArray([6, 2, 4, 3, 7, 1, 3], 5, 0) # [1, 3]
p trimArray([1, 7], 0, 0) # [1,7]