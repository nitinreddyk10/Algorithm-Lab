def trinary_search(arr, target):
    if len(arr) == 0:
        return 0
    else:
        mid1 = len(arr) // 3
        mid2 = len(arr) // 3 * 2
        if arr[mid1] == target or arr[mid2] == target:
            return 1
        elif arr[mid1] > target:
            return trinary_search(arr[:mid1], target)
        elif arr[mid2] < target:
            return trinary_search(arr[mid2 + 1:], target)
        else:
            return trinary_search(arr[mid1 + 1:mid2], target)


n = int(input())
x = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(trinary_search(arr, x))
