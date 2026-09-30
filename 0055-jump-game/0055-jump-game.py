class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_jump = 0
        for i in range(n):
            if max_jump < i:
                return False
            max_jump = max(max_jump,i + nums[i])
        return max_jump >= n-1