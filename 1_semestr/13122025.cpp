#include <iostream>

using namespace std;

int main() {
    int n, k;
    cout << "n= ";
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cin >> k;
    
    for (int i = 0; i < n; i++) {
        if ((i + 1) % k == 0) {
            cout << a[i] << " ";
        }
    }
}

