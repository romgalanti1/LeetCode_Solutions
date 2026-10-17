class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n + 1)] # dp[i][j] represents using the minimum number 
                                              # of first i coins to get to amount j
        for j in range(1, amount + 1):
            dp[0][j] = float("inf") # 0 coins can't make any amount

        for c in range(1,n + 1):
            coin = coins[c-1]
            for j in range(0,amount + 1):
                if coin > j:
                    dp[c][j] = dp[c-1][j]
                else:
                    dp[c][j] = min(1 + dp[c][j-coin],dp[c-1][j])
        
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1
            
                