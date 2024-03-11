# Deque_v1
class Deque_v1:
    def __init__(self):
        self._items = []
    
    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        if self.is_empty():
            print("dequeue is empty")
            return None
        else:
            return self._items.pop()
        
    def remove_rear(self):
        if self.is_empty():
            print("dequeue is empty")
            return None
        else:
            return self._items.pop(0)
        
    def is_empty(self):
        return self.item == []
    
    def size(self):
        return len(self._items)

# Deque_v2_linked-list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        data = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data
    
    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        data = self.rear.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size