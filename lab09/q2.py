objs = list(input("Enter all the objects: ").split())
weights = list(map(int, input("Enter the weights of each objects: ").split()))
profit = list(map(int, input("Enter the profit of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

n = len(objs)
unit_profit = [profit[i]/weights[i] for i in range(n)]
group = [(unit_profit[i], objs[i], weights[i], profit[i]) for i in range(n)]

group.sort(reverse=True)
knap = []
w, p = 0, 0
for i in range(n):
    if w + group[i][2] <= cap:
        knap.append((group[i][1], 1))
        w += group[i][2]
        p += group[i][3]
    else:
        left = cap - w
        knap.append((group[i][1], left/group[i][2]))
        w += left
        p += left*group[i][0]
        break

print()
print("The maximum profit is:", p)
print("The objects that can be put in the knapsack are:", *knap)