class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low , high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hours = sum(math.ceil(p/float(mid)) for p in piles)
            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans