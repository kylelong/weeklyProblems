# https://buttondown.email/cassidoo/archive/all-we-have-to-decide-is-what-to-do-with-the-time-1254/

def uniqueSum(nums):
    no_repeat = lambda x: len(set(list(str(x)))) == len(list(str(x)))
    return sum([x for x in nums if no_repeat(x)])

assert(uniqueSum([1,2,3]) == 6)
assert(uniqueSum([11,22,33]) == 0)
assert(uniqueSum([101,2,3]) == 5)