#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, k;
    cin>>n>>q;
    vector<vector <int>> a(n);  //the most important line
    for(int i = 0; i < n; i++){
        cin>>k;
        a[i].resize(k);
        for(int j = 0; j<k; j++){
            cin>>a[i][j];
        }
    }
    int x, y;
    for(int i = 0; i < q; i++){
        cin>>x>>y;
        cout<<a[x][y]<<endl;
    }
    return 0;
}