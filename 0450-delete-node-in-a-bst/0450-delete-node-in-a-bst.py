# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        def deleterec(root,key):
            if not root:
                return None
            if root.val>key:
                root.left=deleterec(root.left,key)
            elif root.val<key:
                root.right=deleterec(root.right,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    successor=root.right
                    while successor.left:
                        successor=successor.left
                    root.val=successor.val
                    root.right=deleterec(root.right,successor.val)
            return root
        return deleterec(root,key)