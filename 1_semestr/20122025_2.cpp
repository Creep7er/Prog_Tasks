// вывести элементы массива в обратном порядке, умножив каждый элемент на 2

#include <iostream>

using namespace std;

int main(){
    int a[9] = {1,2, 3, 4, 5, 6, 7, 8, 9};
    int b[9];
    int n = sizeof(a) / sizeof(a[0]);
    for(int j = 1; j <= n; j+=1){
        b[j] = 2 * a[n - j];
        cout << b[j] << ",";
    }
}