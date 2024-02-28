from ListNode import ListNode
# using dummy Node
class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems +=1 
        else:
            print("index out of range")

    def append(self, newItem):
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1

        if i >= 0 and i <= self.__numItems-1:
            prev = self.getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            if i == self.__numItems - 1 :
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else :
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__numItems -= 1
            return x
        else :
            return None

    def getNode(self, i:int):
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr

    def __findNode(self, x) -> (ListNode, ListNode):
        __head = prev = self.__tail.next
        curr = prev.next
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev, curr = curr, curr.next
        return (None, None)

    def get(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        if i >= 0 and i <= self.__numItems - 1:
            return self.getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
                return index
        return cnt
    
    def count(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    def extend(self, a):
        for x in a:
            self.append(x)

    def copy(self):
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a

    def reverse(self):
        __head = self.__tail.next
        prev = __head; curr = prev.next; next = curr.next
        curr.next = __head; __head.next = self.__tail; self.__tail = curr
        for i in range(self.__numItems - 1):
            prev = curr; curr = next; next = next.next
            curr.next = prev

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort
        self.clear()
        for element in a:
            self.append(a)

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def printList(self):
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else :
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item

if __name__ == '__main__':
    lst = CircularLinkedList()
    lst.append(30)
    lst.insert(0,20)
    a = [4,3,3,2,1]
    lst.extend(a)
    lst.reverse()
    lst.pop(0)
    print(lst.count(3))
    print(lst.get(2))
    lst.printList()