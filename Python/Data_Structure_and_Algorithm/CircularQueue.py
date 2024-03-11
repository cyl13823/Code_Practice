# CircularQueue_v1
class CircularQueue_v1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.back = -1
    
    def enqueue(self, data):
        if self.is_full():
            print("Circular Queue is full")
        else:
            if self.is_empty():
                self.front = self.back = 0
            else:
                self.back = (self.back + 1) % self.capacity
            self.queue[self.back] = data
        
    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty")
            return None
        else:
            item = self.queue[self.front]
            if self.back == self.front:
                self.back = self.front = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return item
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.back + 1) % self.capacity == self.front
    
    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.back:
            return self.back - self.front + 1
        else:
            return self.capacity - self.front + self.back + 1

# CircularQueue_v2_linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node # Connect front and rear
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty")
            return None
        
        item = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front # Update rear to front
        return item

    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        current = self.front
        if self.front is not None:
            while True:
                count += 1
                current = current.next
                if current == self.front:
                    break
        return count