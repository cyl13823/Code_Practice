#include <stdio.h>
#include <stdlib.h>

// Define Circular Queue structure
#define MAX_QUEUE_SIZE 100
typedef struct {
    int data[MAX_QUEUE_SIZE];
    int front, rear;
    int size;
} CircularQueue;

// Circular Queue operations
void circularEnqueue(CircularQueue *cq, int item) {
    if (cq->size == MAX_QUEUE_SIZE) {
        printf("Circular Queue overflow\n");
        return;
    }
    cq->rear = (cq->rear + 1) % MAX_QUEUE_SIZE;
    cq->data[cq->rear] = item;
    cq->size++;
}

int circularDequeue(CircularQueue *cq) {
    if (cq->size == 0) {
        printf("Circular Queue underflow\n");
        return -1;
    }
    int item = cq->data[cq->front];
    cq->front = (cq->front + 1) % MAX_QUEUE_SIZE;
    cq->size--;
    return item;
}

int main() {
    // Circular Queue example
    CircularQueue cq;
    cq.front = cq.rear = 0;
    cq.size = 0;
    circularEnqueue(&cq, 1);
    circularEnqueue(&cq, 2);
    circularEnqueue(&cq, 3);
    printf("Dequeued from circular queue: %d\n", circularDequeue(&cq));
    printf("Dequeued from circular queue: %d\n", circularDequeue(&cq));

    return 0;
}