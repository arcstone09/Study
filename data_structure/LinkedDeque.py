from CircularLinkedList import CircularLinkedList

class ListDeque:
    def __init__(self):
        self.__deque = CircularLinkedList()

    def enqueue(self, x):
        self.__deque.append(x)
    
    def dequeue(self):
        return self.__deque.pop(0)
    
    def push(self, x):
        self.__deque.insert(0, x)
    
    def pop(self):
        return self.__deque.pop(-1)
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
    
    def rear(self):
        if self.isEmpty():
            return None
        else:
            return self.__deque.get(-1)
    
    def isEmpty(self):
        return self.__deque.isEmpty()
    
    def printDeque(self):
        self.__deque.printList()

