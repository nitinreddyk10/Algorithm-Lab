# Is G a directed acyclic graph (DAG)?

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of directed edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)

visited = set()
# print(graph)

def check_cyclic(graph, node, cycle: tuple):
    global visited

    if node in cycle:
        return True
    visited.add(node)

    for i in graph[node]:
        if len(cycle) == 0 or i != cycle[-1]:
            if check_cyclic(graph, i, cycle+(node,)):
                return True
    return False

for v in vertices:
    if v not in visited:
        if check_cyclic(graph, v, ()):
            print("The graph is not acyclic")
            break
else:
    print("The graph is acyclic")
