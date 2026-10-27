# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            noflip = dfs(node1.right,node2.right) and dfs(node1.left,node2.left)
            flip = dfs(node1.right,node2.left) and dfs(node1.left,node2.right)
            
            return flip or noflip
        
        return dfs(root1,root2)
        