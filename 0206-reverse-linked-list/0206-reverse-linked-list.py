# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        prev=head
        curr=prev.next
        if not curr:
            return prev
        nxt=curr.next
        if not nxt:
            curr.next=prev
            prev.next=None
            return curr
        while nxt:
            curr.next=prev
            prev=curr
            curr=nxt
            nxt=nxt.next
        curr.next=prev
        if head:
            head.next=None
        return curr