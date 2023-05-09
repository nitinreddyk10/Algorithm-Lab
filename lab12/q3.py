# Is G a connected graph.

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

def check_connected(graph, node):
    global visited
    
    if node in visited:
        return
    visited.append(node)

    for i in graph[node]:
        check_connected(graph, i)

if m < n:
    print("The graph is not connected")
    exit()

first = list(graph.keys())[0]
check_connected(graph, first)
if len(visited) == n:
    print("The graph is connected")
else:
    print("The graph is not connected")