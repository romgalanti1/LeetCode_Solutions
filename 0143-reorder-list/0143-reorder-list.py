# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node_stack = []
        node = head
        while node:
            node_stack.append(node)
            node = node.next
        
        n = len(node_stack)
        prev = head

        for i in range(n//2):
            temp = prev.next
            curr = node_stack.pop()
            prev.next = curr
            curr.next = temp
            prev = temp
        
        prev.next = None
        return head