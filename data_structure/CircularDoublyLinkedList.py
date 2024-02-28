from BidirectNode import BidirectNode
# using dummy Node
class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode('dummy', None, None)
        self.__head.next = self.__head
        self.__head.prev = self.__head
        self.__numItems = 0
    
    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            prev.next.prev = newNode
            prev.next = newNode
            self.__numItems +=1 
        else:
            print("index out of range")

    def append(self, newItem):
        newNode = BidirectNode(newItem, self.__head.prev, self.__head)
        self.__head.prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1

        if i >= 0 and i <= self.__numItems -1:
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else :
            return None

    def remove(self, x):
        curr = self.__findNode(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return x
        else :
            return None

    def getNode(self, i:int):
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr

    def __findNode(self, x) -> (BidirectNode, BidirectNode):
        curr = self.__head.next
        while curr != __head:
            if curr.item == x:
                return curr
            else:
                curr = curr.next
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
                return cnt
            cnt += 1
        return -12345
    
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
        a = CircularDoublyLinkedList()
        for element in self:
            a.append(element)
        return a

    def reverse(self):
        prev = self.__head; curr = prev.next; next = curr.next
        self.__head.next = prev.prev; self.__head.prev = curr
        for i in range(self.__numItems):
            curr.next = prev; curr.prev = next
            prev = curr; curr = next; next = next.next

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(a)

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def printList(self):
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

    # 쉽배자 2번
    def contains(self,x) : 
        return self.index(x) != -12345
    
    # 쉽배자 3,4번
    def printInterval(self,i:int, j:int):
        if i>=0 and i<=self.__numItems - 1 and j>=0 and j<= self.__numItems - 1:
            curr = self.getNode(i)
            target = self.getNode(j)
            print(curr.item, end = ' ')
            while curr != target:
                curr = curr.next
                if curr == self.__head:
                    continue
                print(curr.item, end = ' ')
        else :
            print('index error')
        
    # 쉽배자 5번
    def numItemsRecursive(self, node):
        if node == self.__head:
            return 0
        return 1 + numItemsRecursive(node.next)

    def numItems(self):
        cnt = 0
        curr = self.__head.next
        while curr != self.__head:
            cnt += 1
            curr = curr.next
        return cnt
    
    

class CircularDoublyLinkedListIterator:
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
    lst = CircularDoublyLinkedList()
    lst.append(30)
    lst.insert(0,20)
    a = [4,3,3,2,1]
    lst.extend(a)
    lst.reverse()
    lst.pop(0)
    print(lst.count(3))
    print(lst.get(2))
    lst.printList()
    lst.printInterval(4,1)
    k = CircularDoublyLinkedList()
    print(k.numItems())
    lst.numItems()