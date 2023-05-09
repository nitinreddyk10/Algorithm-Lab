import itertools

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

if n <= 2:
    print("*")
    exit()

two_perm = list(itertools.combinations(arr, 2))
sum_perm = []
for perm in two_perm:
    sum_perm.append(sum(perm))

max_sum = max(sum_perm)

max_sum_index = sum_perm.index(max_sum)

pair = two_perm[max_sum_index]

sum1 = pair[0]+arr[0]
sum2 = pair[1]+arr[0]
if sum1 > sum2:
    print(pair[0])
else:
    print(pair[1])
print(len(sum_perm))
