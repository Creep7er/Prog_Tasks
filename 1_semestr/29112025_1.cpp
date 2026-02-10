// Вывести на экран первые n четных чисел массива

#include <iostream>

using namespace std;

int main(){
    int a[10];
    int arraySize = 10;

    for(int i = 0; i < arraySize; i += 1){
        a[i] = 2*i;
        cout << a[i] << " ";
    }

}