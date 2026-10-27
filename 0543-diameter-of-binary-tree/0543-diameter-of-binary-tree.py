# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # longest path between two nodes in tree is depth of left + 1 + depth of right
        # so dfs to find depth in left and dfs to find depth in right and return that + 1
        self.max = float("-inf")
        
        def findDepth(node):
            if not node:
                return 0
            left_depth = findDepth(node.left)
            right_depth = findDepth(node.right)
            self.max = max(self.max,left_depth + right_depth)
            
            return 1 + max(right_depth,left_depth)
        findDepth(root)    
        return self.max