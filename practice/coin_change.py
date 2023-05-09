denoms = list(map(int, input("Enter the denominations: ").split()))
x = int(input("Enter the amount: "))
dp = [0]*(x+1)
for i in range(min(denoms), x+1):
    dp[i] = 1 + min([dp[i-k] for k in denoms if (i-k) >= 0])
print(dp[x])