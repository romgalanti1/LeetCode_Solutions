# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # dfs twice with 2 pointers
        # check if mirrored by going left with one and right with the other
        
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            isMirror = dfs(node1.right,node2.left) and dfs(node1.left,node2.right)
            return isMirror
        return dfs(root,root)
        #[none,2,none,2,none,1,none,2,none,2,none]