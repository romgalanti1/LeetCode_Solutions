class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n)
        prev2 = nums[0]
        if n == 1:
            return prev2
        prev1 = max(nums[0],nums[1])
        rob_i = prev1
        for i in range(2,n):
            rob_i = max(prev1,prev2 + nums[i])
            prev2 = prev1
            prev1 = rob_i
        return rob_i