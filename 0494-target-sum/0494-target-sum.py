class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        S = sum(nums)
        S_P = (target + S)
        if S_P % 2 != 0 or abs(target) > S:
            return 0
        t = S_P // 2
        n = len(nums)
        # dp[i][j] = number of ways to reach j from i nums

        dp = [0] * (t + 1)
        dp[0] = 1
        for num in nums:
            for j in range(t, num - 1, - 1):
                dp[j] += dp[j - num]
        
        return dp[-1]