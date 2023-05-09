// Find minimum spanning tree using Prim's algorithm.

#include <bits/stdc++.h>
using namespace std;

#define INF 1e9

vector<pair<int, int>> prims(vector<vector<int>> &graph, int n)
{
    vector<pair<int, int>> mst;
    int weight = 0;
    vector<int> visited;
    visited.push_back(0);

    while (mst.size() < n-1)
    {
        int min_val = INF, v1 , v2;
        for (int i = 0; i < visited.size(); i++)
        {
            int u = visited[i];
            for (int j = 0; j < graph[u].size(); j++)
            {
                auto it = find(visited.begin(), visited.end(), j);
                if (it == visited.end() && graph[u][j] < min_val)
                {
                    min_val = graph[u][j];
                    v1 = u;
                    v2 = j;
                }
            }
        }
        weight += min_val;
        visited.push_back(v2);
        pair<int, int> edge(v1, v2);
        mst.push_back(edge);
    }

    cout << "Weight of MST: " << weight << endl;

    return mst;
}

int main()
{
    int n, m;
    cout << "Enter the number of vertices: ";
    cin >> n;
    cout << "Vertices starts from 0 to " << n-1 << endl;

    vector<vector<int>> graph(n, vector<int>(n, INF));
    cout << "Enter the number of edges: ";
    cin >> m;
    cout << "Enter 'vertex1 vertex2 weight': eg. '0 1 3' " << endl;
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u][v] = w;
        graph[v][u] = w;
    }

    vector<pair<int, int>> mst = prims(graph, n);
    cout << "MST Edges: " << endl;
    for (auto edge : mst)
    {
        cout << edge.first << " " << edge.second << endl;
    }
    
    return 0;
}