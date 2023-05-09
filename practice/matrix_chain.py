n = int(input("Enter the number of matrices: "))
arr = list(map(int, input("Enter the dimensions: ").split()))
dp = [[float('inf')]*n for i in range(n)]
for i in range(n):
    for j in range(0, n-i):
        if i == 0:
            dp[j][j] = 0
            continue
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j]*arr[k+1]*arr[j+i+1])
print("Minimum number of multiplications:", dp[0][n-1])