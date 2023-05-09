def compl_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            if len(l[j:i]) > 1:
                lists.append((l[:j], l[j: i], l[i:]))
    return lists


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

if arr == sorted(arr):
    print("*")
    exit()

least = n
lst = compl_lists(arr)
for i in lst:
    if len(i[1]) < least and i[0] + sorted(i[1]) + i[2] == sorted(arr):
        least = len(i[1])
        res = i[1]
try:
    print(arr.index(res[0]))
    print(arr.index(res[-1]))
except NameError:
    print("0")
    print(n-1)
