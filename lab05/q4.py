n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr_old = arr.copy()
i, j = 0, n-1
while i < len(arr)//2:
    while arr[i] != arr[j]:
        if arr[i]+arr[i+1] == arr[j]:
            arr[i] += arr[i+1]
            arr.pop(i+1)
        elif arr[j]+arr[j-1] == arr[i]:
            arr[j] += arr[j-1]
            arr.pop(j-1)
        elif i+1 == j and n % 2 == 0 and arr[i] == arr_old[n//2-1] and arr[j] == arr_old[n//2]:
            arr[j] += arr[j-1]
            arr.pop(j-1)
        else:
            break
        j -= 1
    i += 1
    j -= 1

for i in range(len(arr)//2):
    if arr[i] != arr[-i-1]:
        print("*")
        exit()

for a in arr:
    print(a)
