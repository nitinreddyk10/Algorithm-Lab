n = int(input())

arr = [i for i in range(1,n+1)]

while len(arr) != 1:
    if len(arr) % 2 == 0:
        arr = arr[0::2]
    else:
        arr = arr[2::2]

print(arr[0])
