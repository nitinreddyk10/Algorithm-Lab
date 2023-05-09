denoms = list(map(int, input("Enter all denominations: ").split()))
x = int(input("Enter a number: "))
k = len(denoms)

denoms.sort(reverse=True)

coins = []
for i in range(k):
    temp = [0]*i
    remain = x
    for j in range(i, k):
        temp.append(remain // denoms[j])
        remain %= denoms[j]
    if remain == 0:
        coins.append(temp)

if len(coins) == 0:
    print("No Change Possible")
    exit()

min_coins = min(coins, key=sum)

print("\nTo give change:")
print("Denominations:", *denoms)
print("        Coins:", *min_coins)
