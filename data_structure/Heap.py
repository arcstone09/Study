class Heap:
    def __init__(self, list):
        if list == None:
            self.__A = []
        else:
            self.__A = list
    
    def insert(self, x):
        self.__A.append(x)
        self.percolateUp(len(self.__A) - 1)
    
    def percolateUp(self, i):
        parent = (i - 1)//2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.percolateUp(parent)

    def deleteMax(self):
        if not self.isEmpty():
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.percolateDown(0)
            return max
        else :
            return None

    def percolateDown(self, i):
        child = 2 * i + 1
        rightChild = 2 * i + 2
        if child <= len(self.__A) - 1:
            if rightChild <= len(self.__A) - 1 and self.__A[child] < self.__A[rightChild]:
                child = rightChild
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.percolateDown(child)

    def max(self):
        return self.__A[0]

    def buildHeap(self):
        for i in range((len(self.__A) - 2) // 2, -1, -1):
            self.percolateDown(i)

    def size(self):
        return len(self.__A)

    def isEmpty(self):
        return len(self.__A) == 0

    def clear(self):
        self.__A = []

    def printHeap(self):
        print(self.__A)
        
h1 = Heap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.insert(7)
h1.printHeap()