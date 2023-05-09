n = int(input("Enter the number of objects: "))
weights = list(map(int, input("Enter the weights of each objects: ").split()))
profits = list(map(int, input("Enter the profit of each objects: ").split()))
cap = int(input("Enter the capacity of the knapsack: "))

objects = [(weights[i], profits[i], i+1) for i in range(n)]
objects.sort(key=lambda x: x[1]/x[0], reverse=True)

w, p = 0, 0
for i in range(n):
    if w + objects[i][0] < cap:
        print("Put", objects[i][0], "kg of object", objects[i][2])
        p += objects[i][1]
        w += objects[i][0]
    else:
        print("Put", (cap - w), "kg of object", objects[i][2])
        p += (cap - w)/objects[i][0]*objects[i][1]
        w += (cap - w)
        break

print("The maximum profit is:", p)