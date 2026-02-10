#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a;
    int b;
    cin >> a;
    cin >> b;

    double gyp = sqrt((a*a) + (b*b));
    double P = a + b + gyp; 

    cout << gyp << endl << P << endl;
    return 0;
}