n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] * 2 >= arr[j]:
            count += 1

print(count)
