def Knapsackdynamic(M, weight, profit):
    n = 4
    arr = [[0 for i in range(M+1)] for j in range(n+1)]
    
    for i in range(n + 1): 
        for j in range(M + 1): 
            if i == 0 or j == 0: 
                arr[i][j] = 0
            elif weight[i-1] <= j: 
                arr[i][j] = max(profit[i-1]  + arr[i-1][j-weight[i-1]],  arr[i-1][j]) 
            else: 
                arr[i][j] = arr[i-1][j]
                
    return arr[n][M]
                
profit = [3, 4, 5, 6]
weight = [2, 3, 4, 5]
M = 5

Knapsackdynamic(M, weight, profit)
