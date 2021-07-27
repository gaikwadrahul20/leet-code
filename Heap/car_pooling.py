
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        s_heap = []
        e_heap = []
        for trip in trips:
            s_heap.append((trip[1],trip[2],trip[0]))
        heapq.heapify(s_heap)
        current_capacity = 0
        while s_heap:
            (s_loc, e_loc, passengers) = heapq.heappop(s_heap)
            current_capacity += passengers
            heapq.heappush(e_heap, (e_loc, passengers))
            
            while( e_heap and e_heap[0][0] <= s_loc):
                p_passengers = heapq.heappop(e_heap)[1]
                current_capacity -= p_passengers
        
            if current_capacity > capacity:
                return False
        return True
            
            