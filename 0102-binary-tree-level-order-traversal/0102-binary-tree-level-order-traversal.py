# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # bfs while appending to res each level array
        output = []
        q = deque([(root,0)])
        current_level = 0
        current_level_values = []
        if not root:
            return []
        
        while q:
            curr,level = q.popleft()
            
            if current_level == level:
                current_level_values.append(curr.val)
            else:
                output.append(current_level_values)
                current_level += 1
                current_level_values = [curr.val]
                
            if curr.left:
                q.append((curr.left,level + 1))
            if curr.right:
                q.append((curr.right,level + 1))
        
        output.append(current_level_values)
            
        return output