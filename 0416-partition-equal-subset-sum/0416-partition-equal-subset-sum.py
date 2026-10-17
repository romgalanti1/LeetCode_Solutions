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
        dp = [[False] * (target + 1) for _ in range(n)] # dp[i][j] = True <-> can partition first i elements to target j
        dp[0][0] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(target + 1):
                if j < num:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j - num] or dp[i-1][j]
        
        return dp[-1][-1]