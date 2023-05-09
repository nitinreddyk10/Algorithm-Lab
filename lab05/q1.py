n = int(input())
m = int(input())
arr = []

for i in range(n):
    arr += list(map(int, input().split()))

min, max = arr[0], arr[0]

for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print(min)
print(max)
