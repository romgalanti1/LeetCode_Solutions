class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        n = len(nums)
        r = n - 1
        l = 0

        while l < r:
            m = (l + r) // 2
            if m < n - 1 and nums[m] > nums[m+1]:
                return nums[m+1]
            if m > 0 and nums[m] < nums[m-1]:
                return nums[m]
            if first > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return first