# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        low, high = p.val, q.val
        if low > high:
            low, high = high, low 
        
        def rec_lca(node):
            if not node:
                return None

            if node.val >= low and node.val <= high:
                return node
            
            elif node.val > high:
                return rec_lca(node.left)
            
            elif node.val < low:
                return rec_lca(node.right)
        
        result = rec_lca(root)
        return result
                