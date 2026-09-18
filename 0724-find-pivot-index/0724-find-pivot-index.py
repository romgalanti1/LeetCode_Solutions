class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ps=[nums[0]]
        for i in range(1,len(nums)):
            ps.append(ps[i-1]+nums[i])
        for i in range(len(nums)):
            if i==0:
                if 0==(ps[-1]-nums[0]):
                    return 0
            elif i==len(nums)-1:
                if 0==ps[-2]:
                    return len(nums)-1
            elif ps[i-1]==(ps[-1]-ps[i]):
                return i
        return -1