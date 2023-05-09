n1 = int(input())
n2 = int(input())
if n1 == 0 and n2 == 0:
    print("0")
    exit()
arr1 = []
arr2 = []
for i in range(n1):
    arr1.append(int(input()))
for i in range(n2):
    arr2.append(int(input()))

if n1 > 0 and n2 > 0:
    res = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
    while i < n1:
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
    while j < n2:
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
elif n1 <= 0:
    res = arr2
elif n2 <= 0:
    res = arr1

if len(res) % 2 == 1:
    print(res[len(res)//2])
else:
    ans = (res[len(res)//2-1] + res[len(res)//2])/2
    if ans.is_integer():
        print(int(ans))
    else:
        print(ans)
