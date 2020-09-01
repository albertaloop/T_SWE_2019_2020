#ifndef _CIRCULARBUFFER_H_
#define _CIRCULARBUFFER_H_

#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <utility> 
#include <cassert>
#include <string>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

using namespace std;
// It has to be power of 2 but since I don't know what is the required size
// So I put 64 here because my Arduino board is 64 KB.
#define BufferSize = 64
// Circualr buffer is like a 1st add 1st out stack.
template<typename T> 
class CircularBuffer
{
    public:
        // Constructor
        CircularBuffer(unsigned int size);
        // Destructor
        ~CircularBuffer();
        // Check if the circular buffer is full or not.
        bool isFull();
        // Check if the circualr buffer is empty or not.
        bool isEmpty();
        // "Push to stack", add elements to the buffer.
        int Write(T element);
        // Cout how many elements are in the circular buffer currently.
        int numElements();
        // "Pop out elements", remove the 1st added element from the circular buffer.
        T Read();
        // This will return the pointer of nth element. If empty then NULL.
        /*int Peek(int nth_element);*/
        // Check the total capacity of the circular buffer or the remaining capacity.
        size_t Capacity();
        // Check the available size of the circular buffer.
        size_t RemainingSize();
        // Reset the buffer to empty state.
        void Reset();
    private:
        vector<T> *buf;
        // This is a smart pointer function I found online, it can 
        // directly allocate space from memory(not sure).
        /* unique_ptr<T[]> buf_; */
        unsigned int head, tail, num_Elements, size;
        bool full;
        T read;

};

////////////////////////////////////////////////////////////////

// This is the constructor
template <typename T>
CircularBuffer<T>::CircularBuffer(unsigned int size){
    assert(size > 0);
    // I used a vector structure to simulate the buffer structure.
    // However if this is not how we want to store data, we could do:
    /*
    explicit circular_buffer(size_t size) :
    buf_(std::unique_ptr<T[]>(new T[size])),
    max_size_(size)
    {   
        //empty constructor
    }
    */
    buf = new vector<T>[size];
    // Zero at this point because no element in the buffer.
    this->size = size;
    this->head = 0;
    this->tail = 0;
    this->num_Elements = 0;
    this->full = false;
}
// This is the destructor
template <typename T>
CircularBuffer<T>::~CircularBuffer(){
    delete[] buf;
}
// Add element to our structure
template <typename T>
int CircularBuffer<T>:: Write(T element){
    if(isFull()){
        // Do reset or what, I dont know.
    }
    else{
        (*buf)[head] = element;
        head=(head+1) % size;
        cout << head << endl;
        if(head == tail){
            full = true;
        }
    }

}
template <typename T>
T CircularBuffer<T>::Read(){
    if(isEmpty()){
        // No element to read.
    }
    else{
        read = (*buf)[tail];
        tail=(tail+1) % size;
        full = false;
    }

}
// This function is for checking whether the buffer is full or not.
template <typename T>
bool CircularBuffer<T>::isFull(){
    return full;
}
template <typename T>
bool CircularBuffer<T>::isEmpty(){
    bool temp = false;
    if((head == tail)&&(full != true)){
        temp = true;
    }
    return temp;
}
template <typename T>
void CircularBuffer<T>::Reset(){
    head = tail;
    full = false;
}

template <typename T>
size_t CircularBuffer<T>::Capacity(){
    return size;
}

template <typename T>
size_t CircularBuffer<T>::RemainingSize(){
    size_t RemSize = size;
    if(!full){
        if(head >= tail){
            RemSize = head - tail;
        }
        else{
            RemSize = size + head - tail;
        }
    }
    return RemSize;
}
template <typename T>
int CircularBuffer<T>::numElements(){
    int num = static_cast<int>(size);
    if(!full){
        if(head >= tail){
            num = num - (head - tail);
        }
        else{
            num = num - (num + head - tail);
        }
    }
    num_Elements = num;
    return num;
}
/*template <typename T>
int CircularBuffer<T>::Peek(int nth_element){
    int *ret = NULL;
    if(isEmpty() || (nth_element > num_Elements-1)){
        ret = NULL;
    }
    else{
        ret = ((head + nth_element) % size) * size;
    }
    return ret;
}*/
#endif