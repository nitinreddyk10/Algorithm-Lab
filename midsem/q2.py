from string import ascii_uppercase
n = int(input("Enter number of matrix: "))
mat = ascii_uppercase[:n]
dp = [[None for i in range(n)] for j in range(n)]

def add_paren(string):
    string = str(string)
    return '('+string+')'

def res(i,j):
    if i==j:
        dp[i][j] = (str(mat[i]),)
        return dp[i][j]
    
    if dp[i][j] != None:
        return dp[i][j]

    result = []
    for k in range(i,j):
        part1 = res(i,k)
        part2 = res(k+1,j)
        for a in part1:
            for b in part2:
                c = ""
                if len(a) == 1:
                    c += a
                else:
                    c += add_paren(a)
                if len(b) == 1:
                    c += b
                else:
                    c += add_paren(b)
                result.append(c)
    dp[i][j] = tuple(result)
    return dp[i][j]

final = res(0,n-1)
for i, f in enumerate(final):
    print(i+1, f)