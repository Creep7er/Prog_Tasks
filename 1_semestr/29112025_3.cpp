// найдите произведение первых n членов геометрических прогрессий каждого элемента массива

#include <iostream>

using namespace std;

int main(){
    int a[100], n, q, b;
    cin >> a[0] >> n >> q;
    b = a[0];
    cout << endl << "Массив " << a[0] << endl;
    for(int i = 1; i <= n; i += 1){
        a[i] = a[i-1] * q;
        cout << "Массив " << a[i] << endl;
        b = b*a[i];
    }
    cout << "Произведение " << b << endl;
}