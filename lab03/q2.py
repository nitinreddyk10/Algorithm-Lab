n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


min_arr, max_arr = [], []
if n % 2 == 1:
    arr.append(arr[-1])
    n += 1
for i in range(0, n, 2):
    if arr[i] > arr[i+1]:
        min_arr.append(arr[i+1])
        max_arr.append(arr[i])
    else:
        min_arr.append(arr[i])
        max_arr.append(arr[i+1])

min, max = min_arr[0], max_arr[0]
for i in range(1, int(n/2)):
    if min_arr[i] < min:
        min = min_arr[i]
    elif max_arr[i] > max:
        max = max_arr[i]

if min == max:
    print(min)
else:
    print(min)
    print(max)
