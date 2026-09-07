class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        seen = {}
        
        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = (2 * dp[i - 1] + 1) % MOD
            
            if char in seen:
                last_idx = seen[char]
                dp[i] = (dp[i] - dp[last_idx - 1] - 1) % MOD
            seen[char] = i
            
        return dp[n] % MOD