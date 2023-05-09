n = int(input("Enter the number of objects: "))
weights = list(map(int, input("Enter the weights of each objects: ").split()))
profits = list(map(int, input("Enter the profit of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

def max_profit(i, w, p):
    if i>=n:
        return p
    if weights[i]+w < cap:
        return max(max_profit(i+1, w+weights[i], p+profits[i]), max_profit(i+1, w, p))
    else:
        return max_profit(i+1, w, p)

print("The maximum profit is:", max_profit(0, 0, 0))