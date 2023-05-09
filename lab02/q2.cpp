#include <iostream>
#include <set>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];
    set<int> arr_set;
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
        arr_set.insert(arr[i]);
    }

    int min1, min2;
    min1 = min2 = *arr_set.begin();
    for (auto it = arr_set.begin(); it != arr_set.end(); it++)
    {
        if (*it < min1)
        {
            min2 = min1;
            min1 = *it;
        }
        else if (*it < min2)
        {
            min2 = *it;
        }
        if (min1 == min2)
            min2 = *it;
    }
    cout << min1 << endl;
    if (min1 == min2)
        cout << "*" << endl;
    else
        cout << min2 << endl;

    return 0;
}