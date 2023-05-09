# List all maximal strongly connected components in G.

n = int(input("Enter number of vertices: "))
vertices = input("Enter all vertices (like 'a b'): ").split()
graph = {v:[] for v in vertices}

m = int(input("Enter number of directed edges: "))
print("Enter connected edges (like 'a-b'): ")
for i in range(m):
    u, v = input().split('-')
    graph[u].append(v)


def dfs(graph, node, comp):
    global visited2
    visited2.add(node)
    comp.add(node)

    for i in graph[node]:
        if i not in visited2:
            dfs(graph, i, comp)
    
    return comp

def create_dfs_stack(graph, node):
    global visited1, dfs_stk
    visited1.add(node)

    for i in graph[node]:
        if i not in visited1:
            create_dfs_stack(graph, i)
    
    dfs_stk.append(node)
    return dfs_stk

def reverse_graph(graph, stack):
    new_graph = {v:[] for v in vertices}
    for v in stack:
        for i in graph[v]:
            if i in stack:
                new_graph[i].append(v)
    
    return new_graph


visited1 = set()
all_comp = []

for v in vertices:
    if v not in visited1:
        dfs_stk = []
        create_dfs_stack(graph, v)
        rev_graph = reverse_graph(graph, dfs_stk)

        visited2 = set()
        while len(dfs_stk) > 0:
            v = dfs_stk.pop()
            if v not in visited2:
                comp = dfs(rev_graph, v, set())
                all_comp.append(comp)

print("The maximal strongly connected components are:")
for comp in all_comp:
    print(comp)