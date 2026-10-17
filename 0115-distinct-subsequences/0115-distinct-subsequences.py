class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n=len(s),len(t)
        # dp[i][j] = num of subsequence of s[:i] that equal t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(n + 1):
                if j == 0:
                    dp[i][j] = 1
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]