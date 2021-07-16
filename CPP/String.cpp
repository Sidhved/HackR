#include <iostream>
#include <string>
using namespace std;

int main() {
	string a, b;
    cin>>a>>b;

    int l1, l2;
    l1 = a.size();
    l2 = b.size();
    string a1 = a;
    a1[0] = b[0];
    string b1 = b;
    b1[0] = a[0];

    cout<<l1<<" "<<l2<<endl;
    cout<<a+b<<endl;
    cout<<a1<<" "<<b1<<endl;

    return 0;
}