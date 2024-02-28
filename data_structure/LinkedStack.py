from LinkedList import LinkedListBasic

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, newItem):
        self.__list.insert(0, newItem)

    def pop(self):
        return self.__list.pop(0)

    def top(self):
        return self.__list.get(0)

    def isEmpty(self):
        return self.__list.isEmpty()

    def popAll(self):
        self.__list.clear()

    def printStack(self):
        self.__list.printList()

if __name__ == '__main__':
    st1 = LinkedStack()
    st1.push(100)
    st1.push(200)
    print("Top is", st1.top())
    st1.pop()
    st1.push('Monday')
    st1.printStack()
    print(st1.isEmpty())