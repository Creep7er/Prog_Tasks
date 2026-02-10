#include <iostream>
#include <cmath>

using namespace std;

int func(double x) {
    if (x < 0){
        return 0;}
    int n = static_cast<int>(floor(x));
    if (n % 2 == 0){
        return 1;
    } else {
        return -1;
    }
}

int main() {
    double x;
    cout << "Введите Х:";
    cin >> x;
    cout << "F(" << x << "): " << func(x) << endl;

    return 0;
}