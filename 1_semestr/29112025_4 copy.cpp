// дано n. Создайте массив каждое число = сумма всех предыдущих

#include <iostream>

using namespace std;

int main(){
    int a[100], n, A, B, sum;
    cin >> n >> A >> B;
    a[0] = A, a[1] = B;
    cout << a[0] << "," << a[1] << ",";
    for(int i = 3; i < n; i += 1){
        sum += a[i];
        a[i] = a[i-1] + sum;
        cout << a[i] << ",";
    }
}