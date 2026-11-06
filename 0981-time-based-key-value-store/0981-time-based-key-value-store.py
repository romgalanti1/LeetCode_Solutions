class TimeMap(object):# hashmap that maps keys to sorted arrays, sorted by timestamp

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append((timestamp,value))

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.dict[key]
        # binary search to find the time <= timestamp
        lo = 0
        hi = len(arr) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return res

        
#{love:[(10,high),(20,low)]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)