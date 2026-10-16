class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        def roblinear(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            elif n == 2:
                return max(nums[0],nums[1])
            else:
                prev2,prev1 = nums[0], max(nums[0],nums[1])
                rob_i = max(prev2,prev1)
                for i in range(2,n):
                    rob_i = max(prev1,prev2 + nums[i])
                    prev2 = prev1
                    prev1 = rob_i
                return rob_i
        return max(roblinear(nums[1:]),roblinear(nums[:-1]))