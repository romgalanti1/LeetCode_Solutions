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

        dp = [[0] * (t + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1,n + 1):
            num = nums[i - 1]
            for j in range(t + 1):
                if j < num:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-num]
            
        return dp[-1][-1]