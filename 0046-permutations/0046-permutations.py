class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []

        def backtrack(path):
            if len(path) == n:
                output.append(path)
                return
            for num in nums:
                if num not in path:
                    new_path = path + [num]
                    backtrack(new_path)
            return
        backtrack([])
        return output