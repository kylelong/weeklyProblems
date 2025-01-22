def longestSubsequence(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            diff = abs(nums[i] - nums[j])
            if diff == 1:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


assert longestSubsequence([1,2,3,4,5]) == 5
assert longestSubsequence([4,2,3,1,5]) == 2
assert longestSubsequence([10,11,7,8,9,12]) == 3