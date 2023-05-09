pots = list(map(int, input("Enter coins in each pot: ").split()))
n = len(pots)

dp = [[0 for i in range(n)] for j in range(n)]

def max_coins(start, end):
    global dp

    if start > end:
        return 0
    elif start == end:
        return pots[start]

    if dp[start][end] != 0:
        return dp[start][end]

    left = pots[start] + min(max_coins(start + 2, end), max_coins(start + 1, end - 1))
    right = pots[end] + min(max_coins(start + 1, end - 1), max_coins(start, end - 2))

    dp[start][end] = max(left, right)
    return dp[start][end]

print(max_coins(0, n - 1))