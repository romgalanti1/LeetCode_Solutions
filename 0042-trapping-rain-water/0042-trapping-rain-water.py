class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        maxl = height[l]
        maxr = height[r]
        total_rain = 0
        while l < r:
            if maxl < maxr:
                total_rain += max(0,maxl - height[l])
                l += 1
                maxl = max(maxl,height[l])
            else:
                total_rain += max(0,maxr - height[r])
                r -= 1
                maxr = max(maxr,height[r])
        return total_rain