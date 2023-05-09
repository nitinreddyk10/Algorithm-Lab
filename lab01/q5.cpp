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
    
    int m = log(n)/log(3)*10000;
    float l = m/10000.0f;
    printf("%.4f", l);
    return 0;
}