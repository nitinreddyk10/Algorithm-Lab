n = int(input())

# Only having the first, last and the
# difference between each element is enough
start, diff, end = 1, 1, n

while end != start:
    if ((end-start) // diff) % 2 == 0:
        # if the no. of elements b/w "start" and "end" is odd
        start += diff*2
    else:
        end -= diff
    diff *= 2

print(start)