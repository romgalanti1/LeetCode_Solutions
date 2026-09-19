# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        stack1=[root1]
        seq1=[]
        stack2=[root2]
        seq2=[]
        while stack1:
            curr=stack1.pop()
            if not curr.right and not curr.left:
                seq1.append(curr.val)
            else:
                if curr.left:
                    stack1.append(curr.left)
                if curr.right:
                    stack1.append(curr.right)
        while stack2:
            curr=stack2.pop()
            if not curr.right and not curr.left:
                seq2.append(curr.val)
            else:
                if curr.left:
                    stack2.append(curr.left)
                if curr.right:
                    stack2.append(curr.right)
        return seq1==seq2