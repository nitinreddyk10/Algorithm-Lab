n = int(input())
if n == 1:
    print("*")
    exit()
arr = []
counts = dict()
for i in range(n):
    arr.append(int(input()))
    try:
        counts[arr[i]] += 1
    except KeyError:
        counts[arr[i]] = 1

for key, value in counts.items():
    if value >= n//2 + 1:
        print(key)
        break
else:
    print("*")
