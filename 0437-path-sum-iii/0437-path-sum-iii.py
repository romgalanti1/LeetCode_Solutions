# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        paths=Counter({0:1})
        def dfs(node,rs,d):
            if not node:
                return 0
            rs+=node.val
            count=d[rs-targetSum]
            d[rs]+=1
            count+=dfs(node.left,rs,d)
            count+=dfs(node.right,rs,d)
            d[rs]-=1
            return count
        return dfs(root,0,paths)