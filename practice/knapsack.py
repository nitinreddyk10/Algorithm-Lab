weight = list(map(int, input("Enter the weights: ").split()))
value = list(map(int, input("Enter the values: ").split()))
x = int(input("Enter the capacity: "))
n = len(weight)
dp = [[0]*(x+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, x+1):
        if weight[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], value[i-1] + dp[i-1][j-weight[i-1]])
        else:
            dp[i][j] = dp[i-1][j]
print("Maximum value:", dp[n][x])