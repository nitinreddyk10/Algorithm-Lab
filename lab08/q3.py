all_denoms = list(map(int, input("Enter all denominations: ").split()))
x = int(input("Enter a number: "))
k = len(all_denoms)

all_denoms.sort(reverse=True)
changes = [[]]*(x+1)

# print(denoms)

def get_denom(i: int):
    global all_denoms

    denom_i = []
    for a in all_denoms:
        if i >= a:
            denom_i.append(a)
    return denom_i.copy()

def get_change(x: int, denoms: list[int]):
    global changes, k

    if changes[x] != []:
        return changes[x].copy()

    all_coins = []
    for d in denoms:
        val = x - d
        coins = get_change(val, get_denom(val))
        coins[all_denoms.index(d)] += 1
        all_coins.append(coins)
    if len(all_coins) == 0:
        print("No Change Possible")
        exit()
    min_coins = min(all_coins, key=sum)
    changes[x] = min_coins
    return min_coins.copy()


for i in range(1, x+1):
    if i in all_denoms:
        changes[i] = [1 if i == a else 0 for a in all_denoms]
    else:
        get_change(i, get_denom(i))

# print(changes)
change = changes[x]
print("To give change:")
print("Denominations:", *all_denoms)
print("        Coins:", *change)