class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        # sort by ratio wage[i] / quality [i]
        
        pairs = [(float(wage[i]) / quality[i] , quality[i]) for i in range(len(quality))]
        pairs.sort()
        total_quality = 0
        min_cost = float("inf")
        heap = []
        
        for rate, q in pairs:
            total_quality += q
            heapq.heappush(heap,-q)
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            if len(heap) == k:
                min_cost = min(min_cost,rate * total_quality)
        return min_cost