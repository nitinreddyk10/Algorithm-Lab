n = int(input())
z = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

check = 0
for i in range(n):
    x = arr[i]
    try:
        y = arr[arr.index(z-x)]
        if x!=y:
            print(x)
            print(y)
            exit()
        else:
            check = 1
    except ValueError:
        check = 1

if check == 1:
    print("*")