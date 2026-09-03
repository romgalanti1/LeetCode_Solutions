class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n=len(nums1)
        min_nums=min(nums1)
        count_even=sum(1 for x in nums1 if x%2==0)
        
        if (min_nums%2==0):
            if(count_even==n):
                return True
            else:
                return False
        else:
            return True