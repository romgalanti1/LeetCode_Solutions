class MyQueue(object):

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        # push onto push stack _ lifo
        # when pop is called pop from pop_stack fifo
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.pop_stack:
            return self.pop_stack.pop()
        else:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        else:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.pop_stack or self.push_stack:
            empty = False
        else:
            empty = True
        return empty 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()