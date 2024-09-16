def waysToScore(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for score in [2,3,6]:
        for i in range(score, n + 1):
            dp[i] += dp[i - score]
    return dp[n]


assert waysToScore(5) == 1
assert waysToScore(12) == 6
assert waysToScore(6) == 3


