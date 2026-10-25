class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # build min heap of size k ordered by euclidean distance from 0,0
        # O(nlogk) time O(k) space
        heap = []
        for x,y in points:
            distance = math.sqrt((x**2)+(y**2))
            heapq.heappush(heap,(-distance,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        output = []
        while heap:
            d,x,y = heapq.heappop(heap)
            output.append([x,y])
        return output