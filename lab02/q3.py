def merge(arr1, arr2):
    sorted_arr = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            sorted_arr.append(arr1[0])
            arr1.pop(0)
        else:
            sorted_arr.append(arr2[0])
            arr2.pop(0)
    sorted_arr += arr1 + arr2
    return sorted_arr


k = int(input())
arr = [[] for _ in range(k)]
for i in range(k):
    n = int(input())
    for j in range(n):
        arr[i].append(int(input()))

sorted_arr = arr[0]
for i in range(1, k):
    sorted_arr = merge(arr[i], sorted_arr)

print(sorted_arr)
