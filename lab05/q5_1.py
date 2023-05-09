n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))


def palin_arr(arr, i, j):
    while i < len(arr)//2:
        while arr[i] != arr[j]:
            if arr[i]+arr[i+1] == arr[j]:
                arr[i] += arr[i+1]
                arr.pop(i+1)
                j -= 1
            elif arr[j]+arr[j-1] == arr[i]:
                arr[j] += arr[j-1]
                arr.pop(j-1)
                j -= 1
            else:
                left_add = arr.copy()
                left_add[i] += left_add[i+1]
                left_add.pop(i+1)
                left_add, i1, j1 = palin_arr(left_add, i, j-1)
                right_add = arr.copy()
                right_add[j] += right_add[j-1]
                right_add.pop(j-1)
                right_add, i2, j2 = palin_arr(right_add, i, j-1)
                if len(left_add) < len(right_add):
                    arr, i, j = right_add, i2, j2
                else:
                    arr, i, j = left_add, i1, j1
                break
        i += 1
        j -= 1
        return arr, i, j


i, j = 0, n-1
arr = palin_arr(arr, i, j)

for a in arr:
    print(a)
