from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack

# q1 front = stack top
def push(q1 : LinkedQueue, q2 : LinkedQueue, x):
    while not q1.isEmpty():
        q2.enqueue(q1.dequeue())
    q1.enqueue(x)
    while not q2.isEmpty():
        q1.enqueue(q2.dequeue())

# q1 back = stack top(just for practice)
def pop(q1 : LinkedQueue, q2 : LinkedQueue):
    cnt = 0
    while not q1.isEmpty():
        q2.enqueue(q1.dequeue())
        cnt += 1
    for i in range(cnt - 1):
        q1.enqueue(q2.dequeue())
    return q2.dequeue()

# s1 top = queue front
def enqueue(s1 : LinkedStack, s2 : LinkedStack, x):
    while not s1.isEmpty():
        s2.push(s1.pop())
    s1.push(x)
    while not s2.isEmpty():
        s1.push(s2.pop())

# s1 top = queue back
def dequeue(s1 : LinkedStack, s2 : LinkedStack):
    while not s1.isEmpty():
        s2.push(s1.pop())
    returnValue = s2.pop()
    while not s2.isEmpty():
        s1.push(s2.pop())
    return returnValue