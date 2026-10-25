class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers, keep track of max height, if height goes lower thats how much rain water in that
        # index can be trapped
        
        n = len(height)
        l = 0
        r = n - 1
        maxl = height[l]
        maxr = height[r]
        trapped_rain = 0
        
        while l < r:
            if maxl < maxr:
                l += 1
                trapped_rain += max(0,maxl - height[l])
                maxl = max(maxl,height[l])
            else:
                r -= 1
                trapped_rain += max(0,maxr - height[r])
                maxr = max(maxr,height[r])
        return trapped_rain