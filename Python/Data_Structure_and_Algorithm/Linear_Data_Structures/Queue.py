# Queue_v1_using append
class Queue_v1:
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
class Queue_v2:
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

class Queue_v3:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        
        return item

    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count