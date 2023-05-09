# Find the Longest path in undirected Tree.

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)
    graph[v].append(u)


def bfs_last(graph, node):
    q = [node]
    visited = set()
    v = ""
    while len(q) > 0:
        v = q.pop(0)
        for i in graph[v]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    return v

def all_paths(graph, node, path):
    global possible_paths, visited

    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            possible_paths.append(path+'-'+i)
            all_paths(graph, i, path+'-'+i)

visited = set()
last_elem = bfs_last(graph, vertices[0])
possible_paths = [last_elem, ]

all_paths(graph, last_elem, last_elem)
longest = max(possible_paths, key=len)
print("Longest path in the tree: ", end="")
print(longest)