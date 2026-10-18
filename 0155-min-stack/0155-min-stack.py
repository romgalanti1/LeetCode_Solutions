class MinStack(object):

    def __init__(self):
        self.min = float("inf")
        self.min_indx = -1
        self.stack = [] # append to stack tuples (val,indx of minimum)

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        node = (value,self.min_indx) # indx of last min
        if value < self.min:
            self.min = value
            self.min_indx = len(self.stack)
        self.stack.append(node)
        

    def pop(self):
        """
        :rtype: None
        """
        value,index = self.stack.pop()
        if not self.stack:
            self.min = float("inf")
            self.min_indx = -1
            return
        if self.min_indx == len(self.stack):
            self.min = self.stack[index][0]
            self.min_indx = index

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()