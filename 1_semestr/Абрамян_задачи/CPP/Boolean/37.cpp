#include <iostream>
using namespace std;

int main() {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    bool able = (x2 <= x1 + 1 || y2 <= y1 + 1);

    if (able)
        cout << "Может" << endl;
    else
        cout << "Не может" << endl;

    return 0;
}