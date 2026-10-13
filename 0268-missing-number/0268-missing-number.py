class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = n * (n+1) / 2
        for num in nums:
            total_sum -= num
        return total_sum