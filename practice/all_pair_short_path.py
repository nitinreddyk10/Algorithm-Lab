n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix ('inf' for no edge):")
graph = [[float(x) for x in input().split()] for i in range(n)]
dp = [g[:] for g in graph]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
print("All pair shortest path matrix:")
for row in dp:
    print(*row)