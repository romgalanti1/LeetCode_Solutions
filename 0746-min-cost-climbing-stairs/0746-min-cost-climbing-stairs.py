class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp =  [float("inf")] * (n + 1)
        dp[0] = dp[1] = 0
        for i in range(2,n + 1):
            cost_1 = dp[i - 1] + cost[i - 1]
            cost_2 = dp[i - 2] + cost[i - 2]
            dp[i] = min(cost_1,cost_2)
        return dp[-1]
