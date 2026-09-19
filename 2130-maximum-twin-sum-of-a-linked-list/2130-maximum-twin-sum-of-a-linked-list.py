# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        stack=[]
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next
        if not stack:
            return 0
        n=len(stack)
        curr=head
        max_twin_sum=0
        while len(stack)>n/2-1:
            twin=stack.pop()
            if twin.val+curr.val>max_twin_sum:
                max_twin_sum=twin.val+curr.val
            curr=curr.next
        return max_twin_sum