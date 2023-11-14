class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if not self.is_empty():  
            node = self.top.data
            self.top = self.top.next
            popped_value = node.data
            self._size -= 1
            return popped_value 
        return None
    
    def is_empty(self):
        return self.top == None
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        
    def size(self):
        return self._size
    
    def printstack(self):
        node = self.top
        while node != None:
            print(node.data)
            node = node.next
