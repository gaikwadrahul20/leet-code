import math
class Heap:
    
    def __init__(self, n):
        self.heap = [None]*n
        self.size = 0
        self.limit = n
    
    def insert(self, num):
        self.size += 1
        self.heap[self.size -1] = num
        self.swim(self.size -1)

    def swim(self, index):
        parent = math.ceil(index-1)
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            tmp = self.heap[index]
            self.heap[index] = self.heap[parent]
            self.heap[parent] = tmp
            self.swim(parent)
    
    def poll(self):
        val = self.heap[0]
        self.heap[0] = self.heap[self.size -1]
        self.heap[self.size -1] = None
        self.size -= 1
        self.heapify(0)
        return val

    
    def heapify(self, index):
        left = 2 * index + 1
        right = 2* index + 2
        largest = index
        if left < self.size and self.heap[left] > self.heap[index]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        
        if index != largest:
            tmp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = tmp
            self.heapify(largest)

    def build_heap(self, array):
        self.heap = array
        self.size = len(array)
        n = math.ceil(self.size/2) - 1
        for i in range(n, -1, -1):
            self.heapify(i)


class Solution:
    def lastStoneWeight(self, stones):
        obj = Heap(len(stones))
        obj.build_heap(stones)
        while(obj.size > 1):
            stone_1 = obj.poll()
            stone_2 = obj.poll()
            if stone_1 != stone_2:
                obj.insert(stone_1-stone_2)
        if obj.heap[0] is None:
            return 0
        return obj.heap[0]
    
obj = Solution()
print(obj.lastStoneWeight([195,940,193,993,760,587,128,339,955,393,768,666,277,209,737,261,762,11,47,912,905,560,333,55,107,91,424,74,379,827]))

# Failing for one test case
