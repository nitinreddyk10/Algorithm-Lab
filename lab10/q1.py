# This is a candidate for DP because,
# - Overlapping subproblems: x-d1, x-d2 ... x-dn can be overlapping for different x
# - Substructure: All the solutions for x can be obtained by all the solution for x-d1, x-d2 ... x-dn

all_denoms = list(map(int, input("Enter all denominations: ").split()))
x = int(input("Enter a number: "))
k = len(all_denoms)

all_denoms.sort()
dp = [[[0]*k]]+[[]]*x

# print(denoms)

def get_denom(i: int):
    global all_denoms

    denom_i = []
    for a in all_denoms:
        if a < i:
            denom_i.append(a)
        else:
            break
    return denom_i.copy()

def get_change(x: int, denoms: list[int]):
    global dp, k

    all_changes = []
    for i in range(len(denoms)):
        val = x - denoms[i]
        prev_change = dp[val].copy()
        for p in prev_change:
            change = p.copy()
            change[i] += 1
            if change not in all_changes:
                all_changes.append(change.copy())
    
    dp[x] = all_changes.copy()

for i in range(1, x+1):
    get_change(i, get_denom(i))
    if i in all_denoms:
        temp = dp[i]
        temp.insert(0, [1 if i == a else 0 for a in all_denoms])

# print(changes)
change = dp[x]
print("To give change:")
print("Denominations:", *all_denoms)
print("        Coins:", *change[0])
for c in change[1:]:
    print("              ", *c)