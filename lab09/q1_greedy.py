objs = list(input("Enter all the objects: ").split())
weights = list(map(int, input("Enter the weights of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

n = len(objs)
group = [(weights[i], objs[i]) for i in range(n)]
group.sort()
knap = []
w = 0
for i in range(n):
    if w + group[i][0] <= cap:
        knap.append(group[i][1])
        w += group[i][0]
    else:
        break

print()
print("The maximum number of the objects is: ", len(knap))
print("The objects that can be put in the knapsack are: ", *knap)