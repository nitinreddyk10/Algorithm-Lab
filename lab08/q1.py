# A set which forms a matroid (https://en.wikipedia.org/wiki/Matroid) 
# can be used to solve the coin changing problem by using greedy approach.

denoms = list(map(int, input("Enter all denominations: ").split()))
x = int(input("Enter a number: "))
k = len(denoms)

denoms.sort(reverse=True)

coins = []
for d in denoms:
    coins.append(x // d)
    x %= d

# multiply denoms and coins
coin_sum = sum([a*b for a,b in zip(coins, denoms)])

if coin_sum != x:
    print("No Change Possible")
    exit()

print("\nTo give change:")
print("Denominations:", *denoms)
print("        Coins:", *coins)
