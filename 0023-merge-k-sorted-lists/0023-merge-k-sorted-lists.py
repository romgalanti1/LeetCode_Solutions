# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        heap = []
        curr = dummy
        
        for head in lists: #build heap of size k
            if head:
                heapq.heappush(heap,(head.val,head))
        
        while heap and curr:
            val,node = heapq.heappop(heap)
            curr.next = node
            if node:
                node = node.next
                if node:
                    heapq.heappush(heap,(node.val,node))
            curr = curr.next
            
            
        return dummy.next