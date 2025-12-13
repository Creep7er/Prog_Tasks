// дано n. Создайте массив состоящий из первых n числе фибоначи

#include <iostream>

using namespace std;

int main(){
    int a[100], n, q;
    cin >> n;
    a[0] = 1, a[1] = 1;
    cout << a[0] << "," << a[1] << ",";
    for(int i = 2; i < n; i += 1){
        a[i] = a[i-1] + a[i-2];
        cout << a[i] << ",";
    }
}