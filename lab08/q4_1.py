# This is greedy strategy implementaion

denoms = list(map(int, input("Enter all denominations: ").split()))
avail = list(map(int, input("Available coins for each: ").split()))
if 0 in avail:
    print("Invalid Input")
    exit()
x = int(input("Enter a number: "))
k = len(denoms)

comb = [(denoms[i], avail[i]) for i in range(k)]
comb.sort(reverse=True)
denoms, avail = [], []
for a,b in comb:
    denoms.append(a)
    avail.append(b)

coins = []
for i in range(k):
    temp = [0]*i
    remain = x
    for j in range(i, k):
        num = avail[j] if avail[j] < remain//denoms[j] else remain//denoms[j]
        remain -= num*denoms[j]
        temp.append(num)
    if remain == 0:
        coins.append(temp)

if len(coins) == 0:
    print("No Change Possible")
    exit()

min_coins = min(coins, key=sum)

print("\nTo give change:")
print("Denominations:", *denoms)
print("        Coins:", *min_coins)
