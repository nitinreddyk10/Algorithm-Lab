# Greedy approach fails to find the optimal solution in this case also
# because this variant is a subset of previous one.
# This is dynamic programming approach implementation.

all_denoms = list(map(int, input("Enter all denominations: ").split()))
avail = list(map(int, input("Available coins for each: ").split()))
if 0 in avail:
    print("Invalid Input")
    exit()
x = int(input("Enter a number: "))
k = len(all_denoms)

comb = [(all_denoms[i], avail[i]) for i in range(k)]
comb.sort(reverse=True)
all_denoms, avail = [], []
for a,b in comb:
    all_denoms.append(a)
    avail.append(b)
changes = [[]]*(x+1)

# print(denoms)
# print(avail)

def get_denom(i: int):
    global all_denoms

    denom_i = []
    for a in all_denoms:
        if i >= a:
            denom_i.append(a)
    return denom_i.copy()

def get_change(x: int, denoms: list[int]):
    global changes, all_denoms, avail, k

    if changes[x] != []:
        return changes[x].copy()

    all_coins = []
    for d in denoms:
        val = x - d
        coins = get_change(val, get_denom(val))
        if coins == [-1]:
            continue
        coins[all_denoms.index(d)] += 1
        all_coins.append(coins)
    for coins in all_coins:
        for i in range(k):
            if coins[i] > avail[i]:
                all_coins.remove(coins)
                break
    if len(all_coins) != 0:
        min_coins = min(all_coins, key=sum)
    else:
        min_coins = [-1]
    changes[x] = min_coins
    return min_coins.copy()

for i in range(1, x+1):
    if i in all_denoms:
        changes[i] = [1 if i == a else 0 for a in all_denoms]
    else:
        get_change(i, get_denom(i))

# print(changes)
change = changes[x]
if change == [-1]:
    print("No Change Possible")
else:
    print("To give change:")
    print("Denominations:", *all_denoms)
    print("        Coins:", *change)