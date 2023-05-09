import itertools

n = int(input())
arr = [int(input()) for _ in range(n)]

num_comb = []
for i in range(1,n):
    num_comb.extend(list(itertools.combinations(arr, i)))

m = len(num_comb)
num_comb_pair = [[num_comb[i], num_comb[m-i-1]] for i in range(m//2)]

for a in num_comb_pair:
    if sum(a[0]) == sum(a[1]):
        print("YES")
        break
else:
    print("NO")