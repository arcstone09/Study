# Created on 이호석의 iPad.

class BidirectNode:
    def __init__(self, newItem, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = newItem
        self.prev = prevNode
        self.next = nextNode

