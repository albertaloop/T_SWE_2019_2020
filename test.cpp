#include "circular_buffer.h"
#include <iostream>
#include <string>

using namespace std;

int main(){
    int num;
    CircularBuffer<int> buffer(6);
    while(true){
        int num;
        cin >> num;
        buffer.Write(num);
        cout << buffer.Read() << endl;
        cout << buffer.numElements() << endl;
        cout << buffer.Capacity() << endl;
    }
    return 0;
}