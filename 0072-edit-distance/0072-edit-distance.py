class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        # dp[i][j] = min edit distance of word1[:i], word2[:j]
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 :
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]
                
                