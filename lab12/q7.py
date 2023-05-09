# Test for presence of even cycle.

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)
    graph[v].append(u)

visited = []
# print(graph)

def check_even_cycle(graph, node, cycle: tuple):
    global visited

    if node in cycle:
        if (len(cycle) - cycle.index(node)) % 2 == 0:
            return True
        else:
            return False
    visited.append(node)

    for i in graph[node]:
        if len(cycle) == 0 or i != cycle[-1]:
            if check_even_cycle(graph, i, cycle+(node,)):
                return True
    return False

for v in vertices:
    if v not in visited:
        if check_even_cycle(graph, v, ()):
            print("The graph contains an even cycle")
            break
else:
    print("The graph does not contains an even cycle")
