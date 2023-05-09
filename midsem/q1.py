objs = list(input("Enter all the consignments: ").split())
weights = list(map(int, input("Enter the weights of each consignments: ").split()))
cap = list(map(int, input("Enter the capacity of the each Trucks: ").split()))

n = len(objs)
cap.sort()
dp = [[[[-1, [0,0,0,0]]*(cap[-1]+1)]*(cap[-1]+1)]*(cap[-1]+1)]*(n+1)

def max_obj(w1, w2, w3, i):
    if i == n:
        return 0
    if dp[i][w1][w2][w3][0] != -1:
        return dp[i][w1][w2][w3]
    
    f = [[0, []]]*4

    f[0] = max_obj(w1, w2, w3, i+1)

    w = [f[0][0], 0, 0, 0]
    if w1 >= weights[i]:
        f[1] = max_obj(w1-weights[i], w2, w3, i+1)
        w[1] = 1+f[1][0]
    if w2 >= weights[i]:
        f[2] = max_obj(w1, w2-weights[i], w3, i+1)
        w[2] = 1+f[2][0]
    if w3 >= weights[i]:
        f[3] = max_obj(w1, w2, w3-weights[i], i+1)
        w[3] = 1+f[3][0]
    
    max_w = max(w)
    trucks = f[w.index(max_w)][1].copy()
    trucks[w.index(max_w)] += 1
    dp[i][w1][w2][w3] = [max_w, trucks.copy()]
    return dp[i][w1][w2][w3]

ans = max_obj(cap[0], cap[1], cap[2], 0)
print()
print("The maximum number of the objects is: ", ans[0])
print("The objects that can be put in trucks are: ")
for i, a in enumerate(ans[1]):
    print("Truck", i+1, ":", a)