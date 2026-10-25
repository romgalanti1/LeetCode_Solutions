class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        #approach - check every distance between two chairs with two pointers. return max
        max_distance = float("-inf")
        left = 0 
        right = 0
        n = len(seats)
        
        while right < n:
            if seats[right] == 1 and max_distance == float("-inf"):
                max_distance = right
                left = right
            elif seats[right] == 1:
                max_distance = max(max_distance,(right - left) // 2)
                left = right
            right += 1
        max_distance = max(max_distance,n - left - 1)
        return max_distance
            
        #[0,0,0,0,1]-> 4 #first time seeing a chair -> max distance is the distance to the chair
        #[0,1,0,0,1,0,0,0,0,1] -> 2 # in between two chairs max distance is j - i // 2
        #[1,0,0,0] -> 3 # the last chairs distance is n - j + 1 so check 
        # check a total of 3 times for max distance
        
        
        