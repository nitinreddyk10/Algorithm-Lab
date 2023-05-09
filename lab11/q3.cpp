// Find second best minimum spanning tree.

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

int sec_min_i(vector<Edge> edges)
{
    int min = INF, sec_min = INF;
    int min_i = -1, sec_min_i = -1;
    int w;
    for (int i = 0; i < edges.size(); i++)
    {
        w = edges[i].weight;
        if (w < min)
        {
            sec_min = min;
            sec_min_i = min_i;
            min = w;
            min_i = i;
        }
        else if (w < sec_min && w != min)
        {
            sec_min = w;
            sec_min_i = i;
        }
    }
    return sec_min_i;
}

int edges_weight(vector<Edge> edges)
{
    int w = 0;
    for (int i = 0; i < edges.size(); i++)
        w += edges[i].weight;
    return w;
}

vector<Edge> sec_mst(vector<Edge> edges, vector<Edge> mst_edges, int n)
{
    vector<Edge> miss_edges;
    for (int i = 0; i < edges.size(); i++)
    {
        for (int j = 0; j < mst_edges.size(); j++)
        {
            if (edges[i].v1 == mst_edges[j].v1 && edges[i].v2 == mst_edges[j].v2)
                break;
            else if (edges[i].v1 == mst_edges[j].v2 && edges[i].v2 == mst_edges[j].v1)
                break;
            else if (j == mst_edges.size()-1)
                miss_edges.push_back(edges[i]);
        }
    }
    sort(miss_edges.begin(), miss_edges.end(), comp_weight);

    vector<Edge> sec_mst_edges = mst_edges;
    int sec_mst_weight = INF;
    for (int i = 0; i < miss_edges.size(); i++)
    {
        vector<Edge> temp_edges = mst_edges;
        temp_edges.push_back(miss_edges[i]);
        int sec_i = sec_min_i(temp_edges);
        if (sec_i == -1)
            continue;
        
        temp_edges.erase(temp_edges.begin() + sec_i);
        int temp_w = edges_weight(temp_edges);
        if (temp_w < sec_mst_weight)
        {
            sec_mst_edges = temp_edges;
            sec_mst_weight = temp_w;
        }
    }

    return sec_mst_edges;
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
    vector<Edge> sec_mst_edges = sec_mst(edges, mst, n);
    cout << "Second MST Edges: " << endl;
    for (auto edge : sec_mst_edges)
    {
        cout << edge.v1 << " " << edge.v2 << endl;
    }
    cout << "Total weight: " << edges_weight(sec_mst_edges) << endl;
    
    return 0;
}