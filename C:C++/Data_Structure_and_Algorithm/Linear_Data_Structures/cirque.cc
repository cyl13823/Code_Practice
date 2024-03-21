#include <iostream>
using namespace std;

// Define Circular Queue class
#define MAX_QUEUE_SIZE 100
class CircularQueue {
private:
    int data[MAX_QUEUE_SIZE];
    int front, rear;
    int size;
public:
    CircularQueue() {
        front = rear = 0;
        size = 0;
    }
    void circularEnqueue(int item) {
        if (size == MAX_QUEUE_SIZE) {
            cout << "Circular Queue overflow" << endl;
            return;
        }
        rear = (rear + 1) % MAX_QUEUE_SIZE;
        data[rear] = item;
        size++;
    }
    int circularDequeue() {
        if (size == 0) {
            cout << "Circular Queue underflow" << endl;
            return -1;
        }
        int item = data[front];
        front = (front + 1) % MAX_QUEUE_SIZE;
        size--;
        return item;
    }
};

int main() {
    // Circular Queue example
    CircularQueue cq;
    cq.circularEnqueue(1);
    cq.circularEnqueue(2);
    cq.circularEnqueue(3);
    cout << "Dequeued from circular queue: " << cq.circularDequeue() << endl;
    cout << "Dequeued from circular queue: " << cq.circularDequeue() << endl;

    return 0;
}