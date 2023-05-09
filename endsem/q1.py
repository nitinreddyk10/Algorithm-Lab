arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)
# binary search to find the smallest element >= x
def bin_search(subseq, x):
    l = 0
    r = len(subseq) - 1
    while l <= r:
        mid = (l + r) // 2
        if subseq[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    return l

subseq = []
for i in range(n):
    if i == 0 or arr[i] > subseq[-1]:
        subseq.append(arr[i])
    else:
        indx = bin_search(subseq, arr[i])
        subseq[indx] = arr[i]

print("Length of longest increasing subsequence:", len(subseq))
print("Longest increasing subsequence:", *subseq)