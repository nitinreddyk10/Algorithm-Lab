def insert(bst, num):


n = int(input())
bst = []
for i in range(n):
    bst = insert(bst, int(input()))
