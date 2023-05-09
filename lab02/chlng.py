n = int(input())
k = int(input())
arr = []
sum = 0
sum_upto = []

for i in range(n):
    arr.append(int(input()))
    sum += arr[i]
    sum_upto.append(sum)

half_sum = [(sum+k)/2, (sum-k)/2]
if not half_sum[0].is_integer():
    print("*")
    exit()

for s in half_sum:
    if s in sum_upto:
        ind = sum_upto.index(int(s))
        if ind != n-1:
            break
else:
    print("*")
    exit()

print(1)
for a in arr[:ind+1]:
    print(a)
print(2)
for a in arr[ind+1:]:
    print(a)
