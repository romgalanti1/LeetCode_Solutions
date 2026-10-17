class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        S = sum(stones)
        target = S // 2
        n = len(stones)
        #dp[i][j] = True if j can be reached by i stones
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1,n + 1):
            stone = stones[i - 1]
            for j in range(target + 1):
                if stone > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i - 1][j-stone]
        A = target
        while dp[-1][A] == False and A > 0:
            A -= 1
        return S - 2 * A