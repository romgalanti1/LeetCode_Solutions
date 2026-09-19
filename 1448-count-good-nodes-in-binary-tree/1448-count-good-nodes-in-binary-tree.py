# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        good_nodes=0
        max_val=root.val
        stack=[(root,max_val)]
        while stack:
            curr,max_val=stack.pop()
            if curr.val>=max_val:
                good_nodes+=1
            if curr.val>max_val:
                max_val=curr.val
            if curr.left:
                stack.append((curr.left,max_val))
            if curr.right:
                stack.append((curr.right,max_val))
        return good_nodes
