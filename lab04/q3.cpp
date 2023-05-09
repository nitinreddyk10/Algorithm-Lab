#include <iostream>
#include <vector>
using namespace std;

vector<int> merge(vector<int> v1, vector<int> v2)
{
    vector<int> result;
    vector<int>::size_type i = 0, j = 0;
    while (i < v1.size() && j < v2.size())
    {
        if (v1[i] < v2[j])
        {
            if (result.empty() || (result.back() != v1[i]))
                result.push_back(v1[i]);
            i++;
        }
        else if (v1[i] > v2[j])
        {
            if (result.empty() || (result.back() != v2[j]))
                result.push_back(v2[j]);
            j++;
        }
        else
        {
            i++;
            j++;
        }
    }
    while (i < v1.size())
    {
        if (result.empty() || (result.back() != v1[i]))
            result.push_back(v1[i]);
        i++;
    }
    while (j < v2.size())
    {
        if (result.empty() || (result.back() != v2[j]))
            result.push_back(v2[j]);
        j++;
    }
    return result;
}

int main()
{
    int n1, n2;
    cin >> n1 >> n2;
    if (n1 <= 0 && n2 <= 0)
    {
        cout << "0" << endl;
        return 0;
    }
    vector<int> arr1(n1), arr2(n2);
    for (int i = 0; i < n1; ++i)
    {
        cin >> arr1[i];
    }
    for (int i = 0; i < n2; ++i)
    {
        cin >> arr2[i];
    }

    vector<int> result;
    if (n1 > 0 && n2 > 0)
        result = merge(arr1, arr2);
    else if (n1 <= 0)
        result = arr2;
    else
        result = arr1;

    int n = result.size();
    if (n % 2 == 0)
    {
        cout << (result[n / 2 - 1] + result[n / 2]) / 2 << endl;
    }
    else
    {
        cout << result[n / 2] << endl;
    }
}