from ListNode import ListNode
# not using dummy Node
class LinkedListBasic:
    def __init__(self):
        self.__head = None
        self.__numItems = 0
    
    def insert(self, i, newItem):
        if i>0 :
            prev = self.get(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems +=1 

        elif i==0 :
            newNode = ListNode(newItem, self.__head)
            self.__head = newNode
            self.__numItems +=1

    def append(self, newItem):
    
    def pop(self, i)

    def remove(self,newItem)

    def get(self, i)

    def index(self, newItem)

    def isEmpty(self)

    def size(self)

    def clear(self)

    def count(self, newItem)