class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        dp = [0] * (target + 1) # dp[i] = number of ways to get to target i
        dp[0] = 1 # 1 way to get to target 0 -> empty sequence

        for j in range(target + 1):
            for num in nums:
                if num > j:
                    pass
                else:
                    dp[j] += dp[j - num]


        return dp[-1]

