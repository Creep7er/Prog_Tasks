// сформировать массив из первых n чисел, кратных 3, и вывести его элементы.

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    
    for(int j = 3, count = 0; count < n; j += 3, count++) {
        a[count] = j;
        cout << a[count] << " ";
    }
    
    return 0;
}