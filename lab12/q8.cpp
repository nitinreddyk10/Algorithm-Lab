// Implement Dijkstra's algorithm.

#include <bits/stdc++.h>
using namespace std;

#define INF 1e8

vector<int> dijkstra(vector<vector<int>> graph, int src)
{
    int n = graph.size();
    vector<int> visited;
    visited.push_back(src);

    vector<vector<int>> dist(graph);
    for (int i = 0; i < n; i++)
        dist[i][i] = 0;

    while (visited.size() < n-1)
    {
        int min_val = INF, v1, v2;
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
        int dist_till = dist[src][v1] + min_val;
        for (int i = 0; i < n; i++)
            dist[src][i] = min(dist_till + dist[v2][i], dist[src][i]);

        visited.push_back(v2);
    }

    return dist[src];
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
    cout << "Enter 'vertex1 vertex2 distance': eg. '0 1 3' " << endl;
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u][v] = w;
        graph[v][u] = w;
    }

    int src;
    cout << "Enter the source vertex: ";
    cin >> src;
    cout << endl;

    vector<int> dist = dijkstra(graph, src);
    cout << "Minimum distance from " << src << " to: ";
    for (int i = 0; i < n; i++)
    {
        if (i != 0)
            cout << "                            ";
        cout << i << " is " << dist[i] << endl;
    }
    
    return 0;
}