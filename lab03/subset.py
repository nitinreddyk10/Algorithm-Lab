n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

bin = [0]*n


def add_one(bin):
    for i in range(n-1, -1, -1):
        if bin[i] == 0:
            bin[i] = 1
            return bin
        bin[i] = 0


print("\nSubsets (at each line):")
print("𝜙")
for i in range(1, 2**n):
    bin = add_one(bin)
    for j in range(n):
        if str(arr[j])*bin[j] != "":
            print(str(arr[j])*bin[j], end=" ")
    print()
