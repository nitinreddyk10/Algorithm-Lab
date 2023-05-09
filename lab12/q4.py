# List all articulation points in G.

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

def remove_vertex(graph, vertex):
    res_graph = {v:graph[v].copy() for v in graph}
    for i in res_graph[vertex]:
        res_graph[i].remove(vertex)
    res_graph.pop(vertex)

    return res_graph

articulate_points = []
org_no_of_comp = no_of_components(graph)

for v in graph:
    v_removed_graph = remove_vertex(graph, v)
    new_no_of_comp = no_of_components(v_removed_graph)
    if new_no_of_comp > org_no_of_comp:
        articulate_points.append(v)

if len(articulate_points) == 0:
    print("The graph has no articulation points")
else:
    print("Articulation points are:", *articulate_points)