from ListNode import ListNode
# using dummy Node
class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0
    
    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems +=1 
        else:
            print("index out of range")

    def append(self, newItem):
        prev = self.__getNode(self.__numItems-1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    def pop(self, i:int):
        if i >= 0 and i <= self.__numItems-1:
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else :
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1

    def __getNode(self, i:int):
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev, curr = curr, curr.next
        return (None, None)

    def get(self, i:int):
        if self.isEmpty():
            return None
        elif i >= 0 and i <= self.__numItems - 1:
            return self.__getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345
    
    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))

    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a

    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))

    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort
        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0

    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()

if __name__ == '__main__':
    lst = LinkedListBasic()
    lst.append(30)
    lst.insert(0,20)
    lst.printList()
    a = LinkedListBasic()
    a.append(4)
    a.append(3)
    a.append(3)
    a.append(2)
    a .append(1)
    lst.extend(a)
    lst.reverse()
    lst.pop(0)
    print(lst.count(3))
    print(lst.get(2))
    lst.printList()