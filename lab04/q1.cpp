#include <iostream>
using namespace std;

int *merge_sort(int *arr, int n)
{
    if (n == 1)
        return arr;
    int *left = new int[n / 2];
    int *right = new int[n - n / 2];
    for (int i = 0; i < n / 2; i++)
        left[i] = arr[i];
    for (int i = n / 2; i < n; i++)
        right[i - n / 2] = arr[i];
    left = merge_sort(left, n / 2);
    right = merge_sort(right, n - n / 2);
    int *result = new int[n];
    int i = 0, j = 0, k = 0;
    while (i < n / 2 && j < n - n / 2)
    {
        if (left[i] < right[j])
        {
            result[k] = left[i];
            i++;
        }
        else
        {
            result[k] = right[j];
            j++;
        }
        k++;
    }
    while (i < n / 2)
    {
        result[k] = left[i];
        i++;
        k++;
    }
    while (j < n - n / 2)
    {
        result[k] = right[j];
        j++;
        k++;
    }
    return result;
}

int main()
{
    int n;
    cin >> n;
    if (n == 1)
    {
        cout << "*" << endl;
        return 0;
    }

    int arr[n];
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    int *result = merge_sort(arr, n);

    int flag = 0;
    for (int i = 0; i < n; ++i)
    {
        if (result[i] == result[i + n / 2])
        {
            flag = 1;
            cout << result[i] << endl;
            break;
        }
    }

    if (flag == 0)
        cout << "*" << endl;

    return 0;
}