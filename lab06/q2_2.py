n = int(input())
bin_n = bin(n)[2:]

# shift "MSB" to the end
bin_n = bin_n[1:] + '1'

print(int(bin_n, base=2))