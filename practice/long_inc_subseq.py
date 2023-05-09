arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)
# binary search to find the smallest element >= x
def bin_search(subarr, x):
    l = 0
    r = len(subarr) - 1
    while l <= r:
        mid = (l + r) // 2
        if subarr[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    return l

subarr = []
for i in range(n):
    if i == 0 or arr[i] > subarr[-1]:
        subarr.append(arr[i])
    else:
        indx = bin_search(subarr, arr[i])
        subarr[indx] = arr[i]

print("Length of longest increasing subsequence:", len(subarr))
print("Longest increasing subsequence:", *subarr)