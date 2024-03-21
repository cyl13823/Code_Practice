#include <stdio.h>
#include <stdlib.h>

// Define Queue structure
#define MAX_QUEUE_SIZE 100
typedef struct {
    int data[MAX_QUEUE_SIZE];
    int front, rear;
} Queue;

// Queue operations
void enqueue(Queue *q, int item) {
    if ((q->rear + 1) % MAX_QUEUE_SIZE == q->front) {
        printf("Queue overflow\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = item;
}

int dequeue(Queue *q) {
    if (q->front == q->rear) {
        printf("Queue underflow\n");
        return -1;
    }
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    return q->data[q->front];
}

int main() {
    // Queue example
    Queue q;
    q.front = q.rear = 0;
    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);
    printf("Dequeued from queue: %d\n", dequeue(&q));
    printf("Dequeued from queue: %d\n", dequeue(&q));

    return 0;
}