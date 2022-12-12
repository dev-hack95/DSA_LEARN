def knapsack(W, weight, profit, t):
    dp = [0 for i in range(W+1)]
    
    for i in range(t+1):
        for w in range(W, 0, -1):
            if weight[i-1] <= w:
                dp[w] = max(dp[w], dp[ w - weight[i-1] ] + profit[i-1])
 
    return dp[W]

profit=[10, 20, 21, 30, 16]
weight = [3, 5, 5, 8, 4]
W = 20
t = len(val)

knapsack(W, weight, profit, t)
