# Stack version 1
class Stack_v1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None]*capacity # create an empty stack
        self.size = 0
    
    def push(self, item): # push the data to the stack
        if self.is_full():
            print("Stack is full")
        else:
            self.stack[self.size] = item
            self.size += 1

    def pop(self): # pop the data to the stack
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            self.size -= 1
            return self.stack[self.size]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity

# Stack v2_capacity is infinity
class Stack_v2:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Stack v3_using linked-list
class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class Stack_v3:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.size = 0
    
    def push(self, data):
        if self.is_full():
            print("Stack is full")
            return None
        else:
            new_data = Node(data)
            if self.top == None:
                self.top = new_data
            else:
                new_data.next = self.top
                self.top = new_data
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped_data
    
    def is_empty(self):
        return self.top == None
    
    def is_full(self):
        return self.size == self.capacity

# Stack v4_using linked-list_without capacity
class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class Stack_v4:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_data = Node(data)
        if self.top == None:
            self.top = new_data
        else:
            new_data.next = self.top
            self.top = new_data

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
    
    def is_empty(self):
        return self.top == None