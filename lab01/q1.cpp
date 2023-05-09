// Given an unsorted array, an integer z. The objective is to find two integers in the array, say x and y such that x+y=z
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, z;
    cin >> n >> z;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    
    int check = 0;
    for (int i = 0; i < n-1; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (arr[i] == z - arr[j])
            {
                cout << arr[i] << endl;
                cout << arr[j] << endl;
                check++;
                return 0;
            }
        }
    }
    if (check == 0)
        cout << "*";
    
    return 0;
}