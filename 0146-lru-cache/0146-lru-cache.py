class Node:
    def __init__(self,key = None,val = None):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key
        
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
    
    def append(self,new_node):
        last_tail = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        new_node.prev = last_tail
        last_tail.next = new_node
    
    def delete(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def popleft(self):
        curr = self.head.next
        self.delete(curr)
        return curr
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.q = DLL() # left is lru right is mru
        self.map = {} # key -> node in q
    
    def use(self,key):
        node = self.map[key]
        self.q.delete(node)
        self.q.append(node)
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self.use(key)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.use(key)
        else:
            if len(self.map) == self.capacity:
                curr = self.q.popleft()
                del self.map[curr.key]
                
            new_node = Node(key,value)
            self.q.append(new_node)
            self.map[key] = new_node
                
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)