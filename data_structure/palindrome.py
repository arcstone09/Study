from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack

def palindrome(str):
    queue = LinkedQueue()
    stack = LinkedStack()
    flag = True
    for i in str:
        queue.enqueue(i)
        stack.push(i)
    while not stack.isEmpty():
        if queue.dequeue() == stack.pop():
            continue
        else : 
            flag = False
    return flag

print(palindrome('lioninoil'))