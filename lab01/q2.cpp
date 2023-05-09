// Given an unsorted array, an integer z. The objective is to find two integers in the array, say x and y such that x+y=z
#include <iostream>
#include <algorithm>
using namespace std;

int search(int arr[], int start, int end, int x, int z);
int findIndex(int arr[], int x);

int main() {
    int n, z;
    cin >> n >> z;
    int arr[n], sorted[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        sorted[i] = arr[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n-i+1; j++)
        {
            if (sorted[i] > sorted[j])
            {
                int temp = sorted[i];
                sorted[i] = sorted[j];
                sorted[j] = temp;
            }
        }
    }
    
    int y = -1;
    for (int i = 0; i < n; i++)
    {
        y = search(sorted, 0, n, sorted[i], z);
        if (y != -1 && y != i)
        {
            if (findIndex(arr, sorted[y]) > findIndex(arr, sorted[i]))
                cout << sorted[i] << endl << sorted[y] << endl;
            else
                cout << sorted[y] << endl << sorted[i] << endl;
            break;
        }
    }
    if (y == -1)
        cout << "*";

    
    return 0;
}

int search(int arr[], int start, int end, int x, int z)
{
    if (start > end)
        return -1;
    int mid = (start + end) / 2;
    if (arr[mid] + x == z)
    {
        return mid;
    }
    else if (arr[mid] + x > z)
        return search(arr, start, mid-1, x, z);
    else
        return search(arr, mid+1, end, x, z);
}

int findIndex(int arr[], int x)
{
    for (int i = 0;; i++)
    {
        if (arr[i] == x)
            return i;
    }
}