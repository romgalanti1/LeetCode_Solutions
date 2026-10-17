class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [float("inf")] * (amount + 1) # dp[a] -> minimum coins to get amount a
        dp[0] = 0

        for c in range(n):
            coin = coins[c]
            for a in range(coin, amount + 1):
                    dp[a] = min(1 + dp[a - coin],dp[a])

        return dp[-1] if dp[-1] != float("inf") else -1
                    
                        