// вывести элементы массива, меньше нуля, в порядке возрастания индексов и определите их количество

#include <iostream>

using namespace std;

int main() {
    int count = 0;
    int a[10] = {-1, -2, 3, 4, -5, 0, 7, 8, 9, -1};
    int n = sizeof(a) / sizeof(a[0]);
    for(int i = 0; i < n; i++) {
        if(a[i] < 0) {
            cout << a[i] << " ";
            count++;
        }
    }
    cout << endl<< "Количество " << count;
    return 0;
}