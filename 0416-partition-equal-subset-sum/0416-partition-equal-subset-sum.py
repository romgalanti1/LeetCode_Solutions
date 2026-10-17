class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = sum(nums)
        if S % 2 != 0:
            return False

        target = S / 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(target,num - 1,-1):
                    dp[j] = dp[j - num] or dp[j]
        
        return dp[-1]