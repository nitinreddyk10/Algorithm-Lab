// All Pair Shortest Paths

#include <bits/stdc++.h>
using namespace std;

#define INF 1e8

vector<vector<int>> APSP(vector<vector<int>> &graph)
{
    int n = graph.size();

    vector<vector<int>> dist(graph);
    for (int i = 0; i < n; i++)
        dist[i][i] = 0;
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (dist[i][k] != INF && dist[k][j] != INF)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    return dist;
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

    vector<vector<int>> dist = APSP(graph);
    cout << "All Pair Shortest Paths: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}