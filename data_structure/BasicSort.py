import time
import random

# selection sort
def selectionSort(A):
    for last in range(len(A) - 1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A, last):
    max_index = 0
    for i in range(last + 1):
        if A[i] > A[max_index]:
            max_index = i
    return max_index

# bubble sort
def bubbleSort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1]

# insertion sort
def insertionSort(A):
    for i in range(1, len(A)):
        value = A[i]
        while value < A[i - 1] and i >=1 :
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1

a = [1,3,6,5,12,4,31,4,13]
insertionSort(a)
print(a)

b=[1,2,3]
c=b[0]
b[0]=8
print(c)














a = random.choices(range(1,100), k = 10000)

start = time.time()
selectionSort(a)
end = time.time()

