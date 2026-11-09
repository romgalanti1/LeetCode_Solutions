class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        each element of nums can either be in a subset or not be
        for each element recurse by taking or skipping
        """
        n = len(nums)
        output = []

        def backtrack(path,i):
            if i == n:
                output.append(path)
                return

            
            with_num = path + [nums[i]]
            without_num = path
            backtrack(with_num,i + 1)
            backtrack(without_num,i + 1)
            
            return

        backtrack([],0)
        return output