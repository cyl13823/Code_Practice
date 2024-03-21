#include <iostream>
using namespace std;

// Define Stack class
#define MAX_STACK_SIZE 100
class Stack {
private:
    int data[MAX_STACK_SIZE];
    int top;
public:
    Stack() {
        top = -1;
    }
    void push(int item) {
        if (top == MAX_STACK_SIZE - 1) {
            cout << "Stack overflow" << endl;
            return;
        }
        data[++top] = item;
    }
    int pop() {
        if (top == -1) {
            cout << "Stack underflow" << endl;
            return -1;
        }
        return data[top--];
    }
};

int main() {
    // Stack example
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    cout << "Popped from stack: " << s.pop() << endl;
    cout << "Popped from stack: " << s.pop() << endl;

    return 0;
}