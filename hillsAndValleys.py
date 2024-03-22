def hills(nums):
    if len(nums) < 3: return 0
    left, right = nums[0], 0
    hills = 0
    for i in range(1, len(nums) - 1):
        if nums[i] != nums[i - 1]:
            left = nums[i - 1]
        right = next((x for x in nums[i+1:] if x != nums[i]), None)
        curr = nums[i]
        
        if nums[i] != nums[i - 1]:
            if right and curr > left and curr > right:
                hills += 1

    return hills

def valleys(nums):
    if len(nums) < 3: return 0
    left, right = nums[0], 0
    valleys = 0
    for i in range(1, len(nums) - 1):
        if nums[i] != nums[i - 1]:
            left = nums[i - 1]
        right = next((x for x in nums[i+1:] if x != nums[i]), None)
        curr = nums[i]
        
        if nums[i] != nums[i - 1]:
            if right and curr < left and curr < right:
                valleys += 1
        
    return valleys

arr = [1,2,1]
assert(hills(arr) == 1) # returns 1
assert(valleys(arr) == 0) # returns 0

arr = [1,0,1]
assert(hills(arr) == 0) # returns 0
assert(valleys(arr) == 1) # returns 1

arr = [7,6,5,5,4,1]
assert(hills(arr) == 0) # returns 0
assert(valleys(arr) == 0) # returns 0

arr = [3,4,1,1,6,5]
assert(hills(arr) == 2) # returns 2
assert(valleys(arr) == 1) # returns 1