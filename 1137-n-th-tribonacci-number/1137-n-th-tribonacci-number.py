class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        if n<=2:
            return dp[n]
        for i in range(2,n):
            dp.append(dp[i]+dp[i-1]+dp[i-2])
        return dp[-1]