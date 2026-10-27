# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def getHeight(node):
            if not node:
                return -1
            res = 1 + getHeight(node.left)
            return res
        if not root:
            return 0
        
        total = 1
        node = root
        
        while node:
            right_depth = getHeight(node.right)
            left_depth = getHeight(node.left)
            
            if right_depth == left_depth : # left is complete tree continue right
                if right_depth != -1:
                    total += 2 ** (left_depth + 1)
                node = node.right
            else: # right_depth < left_depth, # left is incomplete
                if left_depth != -1:
                    total += 2 ** (right_depth + 1)
                node = node.left
        return total
                    
                
                
        
        
                