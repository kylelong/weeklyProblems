def rotatedNum(nums):
    if not nums:
        return 0
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return 0
    
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left # the rotation point
print(rotatedNum([4, 0, 1, 2, 3]))
print(rotatedNum([7, 9, 20]))
print(rotatedNum([7, 7, 314, 1337, 7]))

'''
Perform a binary search:
    - Find the middle element of the array.
    - If the middle element is greater than the right element, the rotation point is to the right of middle. So, set left to middle + 1.
    - Otherwise, the rotation point is to the left of middle (including the middle itself), so set right to middle.

Continue this process until left equals right. The final position of left (or right) will be the number of times the array has been rotated.
This approach efficiently finds the rotation point even if the array contains duplicates.
'''