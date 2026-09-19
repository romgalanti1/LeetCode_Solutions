# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_length=0
        def dfs(root,left,length):
            if not root:
                return -1
            self.max_length=max(self.max_length,length)
            if left:
                dfs(root.left,False,length+1)
                dfs(root.right,True,1)
            else:
                dfs(root.right,True,length+1)
                dfs(root.left,False,1)
        dfs(root,True,0)
        dfs(root,False,0)
        return self.max_length
