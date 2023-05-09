// Find minimum spanning tree using Kruskal's algorithm.

#include <bits/stdc++.h>
using namespace std;

#define INF 1e9
class Edge
{
public:
    int v1, v2, weight;
    Edge(int v1=-1, int v2=-1, int weight=INF)
    {
        this->v1 = v1;
        this->v2 = v2;
        this->weight = weight;
    }
};

bool comp_weight(Edge e1, Edge e2)
{
    return e1.weight < e2.weight;
}

bool check_cycle(vector<Edge> &edges, int node, vector<int> visited)
{
    auto it = find(visited.begin(), visited.end(), node);
    if (it != visited.end())
    {
        if (*(visited.end()-2) != node)
            return true;
        else
            return false;
    }

    visited.push_back(node);
    int v;
    for (int i = 0; i < edges.size(); i++)
    {
        if (edges[i].v1 == node)
            v = edges[i].v2;
        else if (edges[i].v2 == node)
            v = edges[i].v1;
        else
            continue;
        if (check_cycle(edges, v, visited))
            return true;
    }
    return false;
}

vector<Edge> kruskals(vector<Edge> edges, int n)
{
    vector<Edge> mst_edges;

    sort(edges.begin(), edges.end(), comp_weight);

    while (edges.size() > 0)
    {
        Edge e = edges.front();
        edges.erase(edges.begin());
        mst_edges.push_back(e);

        if (check_cycle(mst_edges, e.v1, vector<int>()))
            mst_edges.pop_back();
    }
    return mst_edges;
}

int main()
{
    int n, m;
    cout << "Enter the number of vertices: ";
    cin >> n;
    cout << "Vertices starts from 0 to " << n-1 << endl;

    vector<Edge> edges;
    cout << "Enter the number of edges: ";
    cin >> m;
    cout << "Enter 'vertex1 vertex2 weight': eg. '0 1 3' " << endl;
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back(Edge(u, v, w));
    }

    vector<Edge> mst = kruskals(edges, n);
    int weight = 0;
    cout << "MST Edges: " << endl;
    for (auto edge : mst)
    {
        cout << edge.v1 << " " << edge.v2 << endl;
        weight += edge.weight;
    }
    cout << "Total weight: " << weight << endl;
    
    return 0;
}