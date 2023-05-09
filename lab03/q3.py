n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.append(int(input()))
for i in range(1, n):
    el = int(input())
    if el < arr[0]:
        arr.insert(0, el)
    elif el > arr[-1]:
        arr.append(el)

print(arr[0])
print(arr[-1])
