def hash(num, i=0):
    global n
    return abs(num + i*i) % n


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

res = []
visited = []
ind, i = 0, 0
while len(visited) < n:
    if ind not in visited:
        visited.append(ind)
        if arr[ind] == ind:
            res.append(ind)
        ind = hash(arr[ind])
        i = 0
    else:
        i += 1
        ind = hash(arr[ind], i=i)

if len(res) == 0:
    print("*")
    exit()

for num in sorted(res):
    print(num)
