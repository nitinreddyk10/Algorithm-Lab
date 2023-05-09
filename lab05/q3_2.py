n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()), i))


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


sorted_arr = sorted(arr)


def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = (len(arr)) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root


def findDouble(root, val):
    if root == None:
        return
    if root.data[0] >= val:
        return root.data
    elif root.data[0] < val:
        return findDouble(root.right, val)


tree = sortedArrayToBST(sorted_arr)

for a in arr:
