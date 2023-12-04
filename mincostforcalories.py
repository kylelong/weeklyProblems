'''
let calories = [200, 400, 600, 800]
let prices = [50, 60, 80, 100]
let dailyGoal = 1200

> minCostForCalories(calories, prices, dailyGoal)
> 160 // the 2nd and 4th items add up to 1200 calories for the minimum cost
'''

def minCostForCalories(calories, prices, dailyGoal):
    n = len(calories)
    maxCalories = sum(calories)
    
    # DP table where dp[i] represents the minimum cost to achieve i calories
    dp = [float('inf')] * (maxCalories + 1)
    dp[0] = 0

    # Fill the DP table
    for i in range(n):
        for j in range(maxCalories, calories[i] - 1, -1):
            dp[j] = min(dp[j], dp[j - calories[i]] + prices[i])

    # Find the minimum cost for the desired calorie goal or more
    result = min(dp[dailyGoal:])
    return result if result != float('inf') else -1

# Example
calories = [200, 400, 600, 800]
prices = [50, 60, 80, 100]
dailyGoal = 1200

minCostForCalories(calories, prices, dailyGoal)

def minCostForCalories(calories, prices, dailyGoal):
    n = len(calories)
    dp = [float('inf')] * (dailyGoal + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(dailyGoal, calories[i] - 1, -1):
            dp[j] = min(dp[j], dp[j - calories[i]] + prices[i])

    return dp[dailyGoal] if dp[dailyGoal] != float('inf') else -1

# Example
calories = [200, 400, 600, 800]
prices = [50, 60, 80, 100]
dailyGoal = 1200

minCostForCalories(calories, prices, dailyGoal)
