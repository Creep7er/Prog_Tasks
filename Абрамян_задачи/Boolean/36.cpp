#include <iostream>
using namespace std;

int main() {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    bool able = (x1 == x2 || y1 == y2);
    
    if (able)
        cout << "Может" << endl;
    else
        cout << "Не может" << endl;

    return 0;
}