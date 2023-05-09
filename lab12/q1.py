# Test for bipartiteness.

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)
    graph[v].append(u)

set1, set2 = set(), set()
visited = []
# print(graph)

def check_bipartite(graph, node, set1: set, set2: set):
    global visited

    if node in visited:
        return True
    visited.append(node)

    set1.add(node)
    for i in graph[node]:
        if i in set1:
            return False
        set2.add(i)
        if not check_bipartite(graph, i, set2, set1):
            return False
    return True

for v in vertices:
    if not check_bipartite(graph, v, set1, set2):
        print("The graph is not bipartite")
        break
else:
    print("The graph is bipartite")