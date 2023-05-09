t = int(input())

for _ in range(t):
    n, m, C = map(int, input().split())
    Ci = [int(x) for x in input().split()]

    lst = []
    for x in range(C):
        lst.extend([x+1]*Ci[x])
    
    matrix = [lst[i:i + m] for i in range(0, len(lst), m)]
    for i in range(n):
        if i%2 == 0:
            for j in range(m):
                print(matrix[i][j], end=" ")
            print()
        else:
            for j in range(m-1, -1, -1):
                print(matrix[i][j], end=" ")
            print()