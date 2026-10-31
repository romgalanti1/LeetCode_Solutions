# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # bfs order traversal while keeping a flag if left to right or right to left
        
        if not root:
            return []
        output = []
        q = deque([root])
        next_level = []
        level_vals = []
        right_to_left = False
        
        while q:
            
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                level_vals.append(node.val)
                
            if right_to_left:
                output.append(level_vals[::-1])
                right_to_left = False
            else:
                output.append(level_vals)
                right_to_left = True
            
            q = next_level
            next_level = []
            level_vals = []
        
        return output
                
                