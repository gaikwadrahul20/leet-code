class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        result = []
        heap_arr = []
        
        i = 0
        for num in nums1:
            heapq.heappush(heap_arr, (num+nums2[i], num, nums2[i]))               
            
        i += 1
        heapq.heapify(heap_arr)
        j = 0
        while heap_arr and j in range(k):
            min_val = heapq.heappop(heap_arr)
            result.append([min_val[1], min_val[2]])
            if i < len(nums2):
                for num in nums1:
                    heapq.heappush(heap_arr, (num+nums2[i], num, nums2[i]))
                i += 1
            j += 1 
        return result
        