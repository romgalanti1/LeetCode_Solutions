# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        """
        preorder - compute root, go left, go right
        in order - go left, compute root, go right
        in preorder, root is the first element, then left subtree then right subtree
        """
        root_to_index = {}
        for i,root_val in enumerate(inorder):
            root_to_index[root_val] = i

        # root is in preorder[0]
        # left subtree of root is inorder[0:root_to_index[preorder[0]]] and right subtree is the right slice
        n = len(inorder)
        def rec(in_start, in_end, pre_start, pre_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            val = preorder[pre_start]
            root = TreeNode(val)
            i = root_to_index[val]
            left_size = i - in_start
            # left subtree is inorder til i right is from i
            root.left = rec(in_start, i - 1,pre_start + 1,pre_end + left_size)
            root.right = rec(i + 1, in_end, pre_start + left_size + 1,pre_end)
            return root
        
        root = rec(0, n - 1, 0, n - 1)
        return root
