n = int(input("Enter number of people: "))
vertices = input("Enter all people (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of friendships: "))
print("Enter friends (like 'a-b'): ")
for i in range(m):
    u, v = input(f"Friendship-{i+1}: ").split('-')
    graph[u].append(v)
    graph[v].append(u)

count = {}
for v in graph:
    if len(v) not in count:
        count[len(v)] = 1
    else:
        count[len(v)] += 1

for i in count.values():
    if i >= 2:
        print(True)
        break
else:
    print(False)