class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # accounts[i][j] = i customer , j bank
        
        n = len(accounts) # n customers
        m = len(accounts[0]) # each customer has m banks
        max_bank = -1
        
        for i in range(n):
            curr_customer = accounts[i]
            customers_wealth = sum(curr_customer)
            max_bank = max(max_bank,customers_wealth)
        
        return max_bank
            
        