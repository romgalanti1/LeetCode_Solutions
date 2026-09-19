# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depths={}
        stack=[root]
        max_depth=0
        curr_depth=0
        if not root:
            return 0
        while stack:
            curr=stack.pop()
            if curr not in depths:
                depths[curr]=curr_depth
                curr_depth+=1
            else:
                curr_depth=depths[curr]
            if curr_depth>max_depth:
                max_depth=curr_depth
            if curr.right and curr.right not in depths:
                stack.append(curr.right)
                depths[curr.right]=curr_depth+1
            if curr.left and curr.left not in depths:
                stack.append(curr.left)
                depths[curr.left]=curr_depth+1
        return max_depth