def rotatedNum(nums):
    sorted_nums, rotations = sorted(nums), 0
    if nums == sorted_nums: return 0
    while nums != sorted_nums:
        first = nums[0]
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        nums[-1] = first
        rotations += 1

    return rotations
print(rotatedNum([4, 0, 1, 2, 3]))
print(rotatedNum([7, 9, 20]))
print(rotatedNum([7, 7, 314, 1337, 7]))

'''
[7, 7, 314, 1337, 7]
[7, 314, 1337, 7, 7]
[314, 1337, 7, 7, 7]
[1337, 7, 7, 7, 314]
[7, 7, 7, 314, 1337]
'''