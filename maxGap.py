'''
Given an integer array arr, return the maximum difference between two successive elements in arr's sorted form. Return 0 if there's 0 or 1 elements.
> maxGap([3,6,9,1,2])
> 3
'''
def maxGap(a):
    if len(a) <= 1: return len(a)
    a.sort()
    return max([a[i+1] - e for i,e in enumerate(a[:-1])])
