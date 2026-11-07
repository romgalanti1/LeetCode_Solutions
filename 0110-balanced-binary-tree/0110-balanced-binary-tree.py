# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # balanced if left height - right height <= 1
        def checkHeight(node):
            if not node:
                return (-1,True)
            left_height, leftBalanced = checkHeight(node.left)
            right_height, rightBalanced = checkHeight(node.right)
            curr_height = 1 + max(left_height,right_height)
            if leftBalanced and rightBalanced and abs(left_height - right_height) <= 1:
                return (curr_height,True)
            else:
                return (curr_height,False)
        
        tree_height,isBalanced = checkHeight(root)

        return isBalanced