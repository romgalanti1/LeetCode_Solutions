# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #level order to string, "root,root.left,root.right,root.left.left..." if no child append #
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        q = deque([root])
        data = []
        while q:
            curr = q.popleft()
            if curr == "#":
                data.append("#,")
            else:
                data.append(str(curr.val) + ",")
                if curr.left:
                    q.append(curr.left)
                else:
                    q.append("#")
                if curr.right:
                    q.append(curr.right)
                else:
                    q.append("#")
        
        return "".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(values[0])
        q = deque([root])
        i = 1
        while q and i < len(values):
            curr = q.popleft()
            if values[i] != "#":
                curr.left = TreeNode(int(values[i]))
                q.append(curr.left)
            i += 1
            if i < len(values):
                if values[i] != "#":
                    curr.right = TreeNode(int(values[i]))
                    q.append(curr.right)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))