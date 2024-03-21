#include <iostream>
using namespace std;

// Define Queue class
#define MAX_QUEUE_SIZE 100
class Queue {
private:
    int data[MAX_QUEUE_SIZE];
    int front, rear;
public:
    Queue() {
        front = rear = 0;
    }
    void enqueue(int item) {
        if ((rear + 1) % MAX_QUEUE_SIZE == front) {
            cout << "Queue overflow" << endl;
            return;
        }
        rear = (rear + 1) % MAX_QUEUE_SIZE;
        data[rear] = item;
    }
    int dequeue() {
        if (front == rear) {
            cout << "Queue underflow" << endl;
            return -1;
        }
        front = (front + 1) % MAX_QUEUE_SIZE;
        return data[front];
    }
};

int main() {
    // Queue example
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << "Dequeued from queue: " << q.dequeue() << endl;
    cout << "Dequeued from queue: " << q.dequeue() << endl;

    return 0;
}