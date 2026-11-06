class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # recursively iterate through candidates, and lower target by candidate

        output = []
        n = len(candidates)

        def rec(nums,i,total):
            if total < 0:
                return
            if total == 0 and nums:
                output.append(nums)
                return
            if i == n:
                return
            for j in range(i,n):
                array = nums + [candidates[j]]
                rec(array,j,total - candidates[j])
            return
        rec([],0,target)
        return output
            