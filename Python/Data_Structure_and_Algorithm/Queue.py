# Queue_v1_using append
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Queue_v2_using insert
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
# Queue_v3_linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None