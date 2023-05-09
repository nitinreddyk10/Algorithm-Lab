# Is G a triangle free graph.

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

def check_triangle(graph, node, prev: str):
    global visited
    
    if node in visited:
        return True
    visited.append(node)

    for i in graph[node]:
        if prev in graph[i]:
            return False
        if not check_triangle(graph, i, node):
            return False

    return True

for v in vertices:
    if not check_triangle(graph, v, ""):
        print("The graph is not triangle-free")
        break
else:
    print("The graph is triangle-free")