
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_largest = []
        self.heap_smallest = []
        

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.heap_largest, num)
        heapq.heappush(self.heap_smallest, -heapq.heappop(self.heap_largest))
        if len(self.heap_largest) < len(self.heap_smallest):
            heapq.heappush(self.heap_largest, -heapq.heappop(self.heap_smallest))
        
    def findMedian(self) -> float:
        n = len(self.heap_smallest)
        m = len(self.heap_largest)
        if m == n:
            return (self.heap_largest[0] + (-self.heap_smallest[0]))/2.0
        else:
            return self.heap_largest[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

