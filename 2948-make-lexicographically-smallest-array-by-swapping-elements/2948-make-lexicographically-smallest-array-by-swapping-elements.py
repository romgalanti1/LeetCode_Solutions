import math
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        groups=[]
        gmap={}
        for num in sorted(nums):
            if not groups or abs(num-groups[-1][-1])>limit:
                groups.append([])
            groups[-1].append(num)
            gmap[num]=len(groups)-1
        itr=[iter(g) for g in groups]
        for i in range(len(nums)):
            nums[i]=next(itr[gmap[nums[i]]])
        return nums