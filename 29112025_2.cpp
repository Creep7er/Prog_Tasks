// сделать арифметическую прогрессию

#include <iostream>

using namespace std;

int main(){
    int a[100], n, d;
    cin >> a[0] >> n >> d;
    cout << a[0] << " ";
    for(int i = 1; i <= n; i += 1){
        a[i] = a[i-1] + d;
        cout << a[i] << " ";
    }

}