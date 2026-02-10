#include <iostream>

using namespace std;

int main(){
    int a[10] = {1, 2,3,4,5,6,7,8,9,0};
    int arraySize = sizeof(a) / sizeof(a[0]);

    for(int t = 0; t < arraySize; t++){
        cin >> a[t];
    }

    for(int i = 0; i < arraySize; i++){
        cout << a[i] << endl;
    }
}