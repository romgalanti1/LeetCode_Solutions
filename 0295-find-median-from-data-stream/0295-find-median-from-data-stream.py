class MedianFinder(object):
    # hold two heaps, one min heap and one max heap
    # keep sizes the same or 1 more to the max heap
    # min heap the greater half max heap holds the smaller half
    # if both heaps same size median is half of the sum of min and max
    # if max heap is one more median is max

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap,-num)
        mid = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,mid)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
                
                    

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            s = self.min_heap[0] + -self.max_heap[0]
            return s / 2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()