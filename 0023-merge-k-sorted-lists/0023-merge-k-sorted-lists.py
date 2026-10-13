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
        pq = []
        for idx , node in enumerate(lists):
            if node:
                pq.append((node.val,idx,node))
        heapq.heapify(pq)
        dummy = ListNode()
        temp = dummy
        while pq:
            val,idx,node = heapq.heappop(pq)
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                heapq.heappush(pq,(node.val,idx,node))
        return dummy.next