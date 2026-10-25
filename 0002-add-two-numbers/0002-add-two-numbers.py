# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # add numbers while keeping a carry
        p1 = l1
        p2 = l2
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            value_sum = val1 + val2 + carry
            carry = value_sum // 10
            nxt = ListNode(value_sum % 10)
            curr.next = nxt
            curr = nxt
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
    
        return dummy.next