#include <iostream>
using namespace std;

// Define Deque class
#define MAX_DEQUE_SIZE 100
class Deque {
private:
    int data[MAX_DEQUE_SIZE];
    int front, rear;
public:
    Deque() {
        front = rear = MAX_DEQUE_SIZE / 2;
    }
    void enqueueFront(int item) {
        if ((front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE == rear) {
            cout << "Deque overflow" << endl;
            return;
        }
        data[front] = item;
        front = (front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
    }
    void enqueueRear(int item) {
        if ((rear + 1) % MAX_DEQUE_SIZE == front) {
            cout << "Deque overflow" << endl;
            return;
        }
        rear = (rear + 1) % MAX_DEQUE_SIZE;
        data[rear] = item;
    }
    int dequeueFront() {
        if (front == rear) {
            cout << "Deque underflow" << endl;
            return -1;
        }
        front = (front + 1) % MAX_DEQUE_SIZE;
        return data[front];
    }
    int dequeueRear() {
        if (front == rear) {
            cout << "Deque underflow" << endl;
            return -1;
        }
        int item = data[rear];
        rear = (rear - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
        return item;
    }
};

int main() {
    // Deque example
    Deque dq;
    dq.enqueueFront(1);
    dq.enqueueFront(2);
    dq.enqueueRear(3);
    cout << "Dequeued from deque front: " << dq.dequeueFront() << endl;
    cout << "Dequeued from deque rear: " << dq.dequeueRear() << endl;

    return 0;
}