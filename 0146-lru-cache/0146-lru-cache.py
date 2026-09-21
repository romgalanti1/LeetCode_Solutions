class Node(object):
    def __init__(self,val = -1,key = -1):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {} # key -> node
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def append(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            self.remove(node)
            self.append(node)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.append(node)
            node.val = value
        else:
            if len(self.map) >= self.capacity:
                lru = self.head.next
                del self.map[lru.key]
                self.remove(lru)
            node = Node(value,key)
            self.map[key] = node
            self.append(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)