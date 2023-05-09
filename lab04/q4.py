def median(lst):
    n = len(lst)
    if n % 2:
        return lst[n//2]
    return (lst[n//2] + lst[n//2 - 1]) / 2


def find_median(A, B, n1, n2):
    n = n1 + n2
    half_n = n // 2

    l, r = 0, n1 - 1
    while True:
        i = (l + r) // 2
        j = half_n - i - 2

        a_left = A[i] if i >= 0 else float('-infinity')
        a_right = A[i+1] if i+1 < n1 else float('infinity')
        b_left = B[j] if j >= 0 else float('-infinity')
        b_right = B[j+1] if j+1 < n2 else float('infinity')

        if a_left <= b_right and a_right >= b_left:
            if n % 2:
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            r = i - 1
        else:
            l = i + 1


n1 = int(input())
n2 = int(input())
if n1 == 0 and n2 == 0:
    print(0)
    exit()
arr1 = []
for i in range(n1):
    arr1.append(int(input()))
arr2 = []
for i in range(n2):
    arr2.append(int(input()))

if n1 == 0:
    med = median(arr2)
elif n2 == 0:
    med = median(arr1)
else:
    if arr2 < arr1:
        arr1, arr2 = arr2, arr1
        n1, n2 = n2, n1
    med = find_median(arr1, arr2, n1, n2)
if float(med).is_integer():
    print(int(med))
else:
    print(med)
