#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> arr;
    int k;
    cin >> k;
    for (int i = 0; i < k; ++i)
    {
        int n;
        cin >> n;
        for (int j = 0; j < n; ++j)
        {
            int num;
            cin >> num;
            arr.push_back(num);
        }
    }
    sort(arr.begin(), arr.end());
    for (int i : arr)
        cout << i << endl;
}