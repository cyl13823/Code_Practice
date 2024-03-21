#include <stdio.h>
#include <stdlib.h>

// Define Stack structure
#define MAX_STACK_SIZE 100
typedef struct {
    int data[MAX_STACK_SIZE];
    int top;
} Stack;

// Stack operations
void push(Stack *s, int item) {
    if (s->top == MAX_STACK_SIZE - 1) {
        printf("Stack overflow\n");
        return;
    }
    s->data[++(s->top)] = item;
}

int pop(Stack *s) {
    if (s->top == -1) {
        printf("Stack underflow\n");
        return -1;
    }
    return s->data[(s->top)--];
}

int main() {
    // Stack example
    Stack s;
    s.top = -1;
    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    printf("Popped from stack: %d\n", pop(&s));
    printf("Popped from stack: %d\n", pop(&s));

    return 0;
}