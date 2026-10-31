# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # all nodes in left subtree are strictly lesser
        # all nodes in right subtree are strictly greater than node.val so need to pass down in dfs
        # dfs down while keeping boundaries
        
        def dfs(node,left_bound,right_bound):
            if not node:
                return True
            if node.val <= left_bound or node.val >= right_bound:
                return False
            
            is_valid = dfs(node.right,node.val,right_bound) and dfs(node.left,left_bound,node.val)
            
            return is_valid
        return dfs(root,float("-inf"),float("inf"))