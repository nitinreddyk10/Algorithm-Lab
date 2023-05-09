n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
min2_arr = []

if n == 1:
    # print(arr[0])
    print("*")
    exit()


def next_min(arr):
    min_arr = []
    m = len(arr)
    if m == 1:
        return arr[0]
    if m % 2 == 0:
        for i in range(0, m, 2):
            if arr[i+1] > arr[i]:
                min_arr.append(arr[i])
            else:
                min_arr.append(arr[i+1])
    else:
        for i in range(0, m-2, 2):
            if arr[i] < arr[i+1]:
                min_arr.append(arr[i])
            else:
                min_arr.append(arr[i+1])
        min_arr.append(arr[-1])
    min = next_min(min_arr)
    if arr.index(min) % 2 == 0:
        if arr[-1] == min and m % 2 == 1:
            return min
        min2_arr.append(arr[arr.index(min)+1])
    else:
        min2_arr.append(arr[arr.index(min)-1])

    return min


print(next_min(arr))
print(next_min(min2_arr))
