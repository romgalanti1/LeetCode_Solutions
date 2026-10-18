class Logger(object):

    def __init__(self):
        self.map = {} # unique message - > time it was printed

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.map:
            self.map[message] = timestamp
            return True
        else:
            last_time = self.map[message]
            if last_time + 10 > timestamp:
                return False
            else:
                self.map[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)