objs = list(input("Enter all the objects: ").split())
weights = list(map(int, input("Enter the weights of each objects: ").split()))
profit = list(map(int, input("Enter the profit of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

n = len(objs)

# DP for 0-1 knapsack
# dp[i][j] = max profit for first i objects with capacity j
dp = [[0]*(cap+1)]*(n+1)
for i in range(1, n+1):
    for j in range(1, cap+1):
        if j >= weights[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + profit[i-1])
        else:
            dp[i][j] = dp[i-1][j]

# print the knapsack
knap = []
w, p = cap, dp[n][cap]
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        knap.append(objs[i-1])
        w -= weights[i-1]
knap.reverse()
print("The maximum profit is:", p)
print("The objects that can be put in the knapsack are:", *knap)