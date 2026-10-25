class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            if len(heap) == k and num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
            elif len(heap) < k:
                heapq.heappush(heap,num)
        return heap[0]
        
        
        
                