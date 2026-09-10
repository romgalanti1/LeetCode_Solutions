# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_size(root):
            if root is None:
                return 0,0
            left_sum,left_size=sum_size(root.left)
            right_sum,right_size=sum_size(root.right)
            root_sum,root_size=root.val+left_sum+right_sum,1+left_size+right_size
            return root_sum,root_size
        stack=[]
        stack.append(root)
        res=0
        curr=root.left
        while stack or curr:
            while curr :
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            curr_sum,curr_size=sum_size(curr)
            curr_avg= curr_sum//curr_size
            if curr.val==curr_avg:
                res+=1
            curr=curr.right
        return res