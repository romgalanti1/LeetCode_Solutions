# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        curr_level=0
        max_level=1
        max_sum=root.val
        queue=[root]
        while queue:
            curr_sum=0
            curr_level+=1
            next_level=[]
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                curr_sum+=node.val
            if curr_sum>max_sum:
                max_sum=curr_sum
                max_level=curr_level
            queue=next_level
        return max_level