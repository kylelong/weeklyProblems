def separateAndSort(nums):
	even = [x for x in nums if x % 2 == 0]
	odd = [x for x in nums if x % 2 != 0]
	even.sort()
	odd.sort()
	return [even, odd]
