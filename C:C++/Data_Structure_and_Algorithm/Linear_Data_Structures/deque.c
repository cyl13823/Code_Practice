#include <stdio.h>
#include <stdlib.h>

// Define Deque structure
#define MAX_DEQUE_SIZE 100
typedef struct {
    int data[MAX_DEQUE_SIZE];
    int front, rear;
} Deque;

// Deque operations
void enqueueFront(Deque *dq, int item) {
    if ((dq->front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE == dq->rear) {
        printf("Deque overflow\n");
        return;
    }
    dq->data[dq->front] = item;
    dq->front = (dq->front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
}

void enqueueRear(Deque *dq, int item) {
    if ((dq->rear + 1) % MAX_DEQUE_SIZE == dq->front) {
        printf("Deque overflow\n");
        return;
    }
    dq->rear = (dq->rear + 1) % MAX_DEQUE_SIZE;
    dq->data[dq->rear] = item;
}

int dequeueFront(Deque *dq) {
    if (dq->front == dq->rear) {
        printf("Deque underflow\n");
        return -1;
    }
    dq->front = (dq->front + 1) % MAX_DEQUE_SIZE;
    return dq->data[dq->front];
}

int dequeueRear(Deque *dq) {
    if (dq->front == dq->rear) {
        printf("Deque underflow\n");
        return -1;
    }
    int item = dq->data[dq->rear];
    dq->rear = (dq->rear - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
    return item;
}

int main() {
    // Deque example
    Deque dq;
    dq.front = dq.rear = MAX_DEQUE_SIZE / 2;
    enqueueFront(&dq, 1);
    enqueueFront(&dq, 2);
    enqueueRear(&dq, 3);
    printf("Dequeued from deque front: %d\n", dequeueFront(&dq));
    printf("Dequeued from deque rear: %d\n", dequeueRear(&dq));

    return 0;
}