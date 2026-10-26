"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # use hashset for node: new_node
        # iterate once pointing to nexts in new LL
        # iterate second time through randoms
        
        
        dummy = ListNode()
        curr = dummy
        node_to_new = {}
        p = head
        
        while p:
            new_node = ListNode(p.val)
            node_to_new[p] = new_node
            curr.next = new_node
            p = p.next
            curr = curr.next
        
        p = head
        curr = dummy.next
        
        while p:
            random_node = p.random
            if random_node:
                curr.random = node_to_new[random_node]
            else:
                curr.random = None
            curr = curr.next
            p = p.next
            
        return dummy.next
            
            
        
        
                