// A program to compute log base 3 for a given integer n
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    string str = to_string(log(n)/log(3.0));
    cout << str.substr(0, str.size()-2);
    return 0;
}