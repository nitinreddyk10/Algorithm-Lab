n = int(input())
arr_set = set()
for i in range(n):
    arr_set.add(int(input()))
arr_sort = sorted(arr_set)
print(arr_sort[0])
try:
    print(arr_sort[1])
except IndexError:
    print('*')
