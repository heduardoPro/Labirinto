class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def isempty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def peek(self):
        if self.isempty() == False:
            return self.top

    def push(self, value:int):
        node = Node(value)
        node.next = self.top
        self.top = node

        self._size += 1 

    def pop(self):
        if self.isempty():
            print("Stack is empty.")
        
        node = self.top
        self.top = self.top.next
        self._size -= 1

        return node
    
    def printall(self):
        current = self.top
        