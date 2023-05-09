n = int(input("Enter the number of objects: "))
weights = list(map(int, input("Enter the weights of each objects: ").split()))
profits = list(map(int, input("Enter the profit of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

dp = [[0]*(cap) for i in range(n)]

for i in range(n):
    for j in range(cap):
        if weights[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + profits[i])
        else:
            dp[i][j] = dp[i-1][j]

print("The maximum profit is:", dp[n-1][cap-1])