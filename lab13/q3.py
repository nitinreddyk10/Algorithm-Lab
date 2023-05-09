# Find the Longest path in DAG.

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of directed edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)


def topo_sort(graph, node):
    global visited, topo
    visited.add(node)

    for i in graph[node]:
        if i not in visited:
            topo_sort(graph, i)
    
    topo.append(node)

def all_paths(graph, topo):
    global possible_paths
    for i in range(len(topo)):
        path = topo[i]
        for j in range(i+1, len(topo)):
            if topo[j] in graph[path[-1]]:
                path += '-'+topo[j]
        possible_paths.append(path)

visited = set()
topo = []
for v in vertices:
    if v not in visited:
        topo_sort(graph, v)
topo.reverse()
possible_paths = []

all_paths(graph, topo)
longest = max(possible_paths, key=len)
print("Longest path in the tree: ", end="")
print(longest)