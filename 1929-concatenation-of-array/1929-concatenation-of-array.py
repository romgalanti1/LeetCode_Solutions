class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        length = 2 * n - 1
        ans = [0] * length
        ans[:n] = nums
        ans[n:] = nums
        return ans