# List all bridges in G.

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

def no_of_components(graph):
    global visited
    count = 0
    for i in graph:
        if i not in visited:
            count += 1
            check_connected(graph, i)
    visited = []
    return count

def remove_edge(graph, v1, v2):
    res_graph = {v:graph[v].copy() for v in graph}
    res_graph[v1].remove(v2)
    res_graph[v2].remove(v1)
    return res_graph

bridges = []
org_no_of_comp = no_of_components(graph)

for v1 in graph:
    for v2 in graph[v1]:
        if v2+'-'+v1 in bridges:
            continue
        e_removed_graph = remove_edge(graph, v1, v2)
        new_no_of_comp = no_of_components(e_removed_graph)
        if new_no_of_comp > org_no_of_comp:
            bridges.append(v1+'-'+v2)

if len(bridges) == 0:
    print("The graph has no Bridges")
else:
    print("Bridges are:", *bridges)