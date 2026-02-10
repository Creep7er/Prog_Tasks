//Вывсти элементы массива в поряжке A[n-1], A[n-2], A[0], A[1], A[n-3], A[n-4]
#include <iostream>

using namespace std;

int main() {
    int a[10] = {0,1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(a) / sizeof(a[0]);
    
    for(int i = 0; i < n/2; i++) {
        cout << a[n - 1 - 2*i] << " ";  // A[n-1], A[n-3], A[n-5]
        if(n - 2 - 2*i >= 0) {
            cout << a[n - 2 - 2*i] << " ";  // A[n-2], A[n-4], A[n-6]
        }
        
        cout << a[2*i] << " ";  // A[0], A[2], A[4]
        if(2*i + 1 < n) {
            cout << a[2*i + 1] << " ";  // A[1], A[3], A[5]
        }
    }
    
    return 0;
}
